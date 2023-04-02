from EdgeGPT import CONVERSATION_STYLE_TYPE, Chatbot
from typing import List, Dict, DefaultDict
import os, re

from src import log

logger = log.setup_logger(__name__)

class BingAgent:
    def __init__(self) -> None:
        self.model_name:str = "bing"
        self.conversation_style_of:DefaultDict[str, CONVERSATION_STYLE_TYPE] = DefaultDict(lambda:"balanced")
        self.bot_of:DefaultDict[str, Chatbot] = DefaultDict(lambda:Chatbot(os.getenv("COOKIE_FILE")))
    
    async def ask(self, context_id:str, message:str):
        try:
            resp = await self.bot_of[context_id].ask(message, conversation_style=self.conversation_style_of[context_id])
            logger.info(f"Response: {resp}")
            return self.__build_reply(resp)
        except Exception as e:
            logger.error(f"Error: {e}")
            return "> **Error: Something went wrong, please reset the conversation or try again later!**"
    
    def switch_style(self, context_id:str, style:CONVERSATION_STYLE_TYPE):
        self.conversation_style_of[context_id] = style
    
    async def reset(self, context_id:str):
        await self.bot_of[context_id].reset()
    
    def __build_reply(self, response:str):
        reply:str = response["item"]["messages"][1]["adaptiveCards"][0]["body"][0]["text"]
        reply = re.sub(r'http[s]?://\S+', lambda x:f"<{x.group(0)}>", reply)
        reply = re.sub(r'\[\^\d+\^]', '', reply)
        reply += "\nSuggested response:\n"
        for suggestion in response["item"]["messages"][1]["suggestedResponses"]:
            reply += f"- {suggestion['text']}\n"
        return reply
    
bing_agent:BingAgent = BingAgent()
