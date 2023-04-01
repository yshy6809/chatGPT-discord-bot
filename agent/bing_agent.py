from EdgeGPT import CONVERSATION_STYLE_TYPE, Chatbot
from typing import List, Dict, DefaultDict
import os

from src import log

logger = log.setup_logger(__name__)

class BingAgent:
    def __init__(self) -> None:
        self.model_name:str = "bing"
        self.conversation_style_of:DefaultDict[str, CONVERSATION_STYLE_TYPE] = DefaultDict(lambda:"balanced")
        self.bot_of:DefaultDict[str, Chatbot] = DefaultDict(lambda:Chatbot(os.getenv("COOKIE_FILE")))
    
    async def ask(self, context_id:str, message:str):
        resp = await self.bot_of[context_id].ask(message, conversation_style=self.conversation_style_of[context_id])
        logger.info(f"Response: {resp}")
        return resp["item"]["messages"][1]["adaptiveCards"][0]["body"][0]["text"]
    
    def switch_style(self, context_id:str, style:CONVERSATION_STYLE_TYPE):
        self.conversation_style_of[context_id] = style
    
    async def reset(self, context_id:str):
        await self.bot_of[context_id].reset()
    
bing_agent:BingAgent = BingAgent()
