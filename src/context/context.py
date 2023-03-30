from typing import DefaultDict, List, Dict
import os
from collections import defaultdict
from  src.context.chat_message import ChatMessage

class ChatContext:
    def __init__(self):
        self.chat_history_of:DefaultDict[str, List[ChatMessage]] = defaultdict(list)
        self.conversation_id_of:DefaultDict[str, str] = defaultdict(str)
        self.parent_id_of:DefaultDict[str, str] = defaultdict(str)
        self.global_model:str = os.getenv("CHAT_MODEL").strip() + " " + os.getenv("GPT_ENGINE")

class ContextManager:
    def __init__(self):
        self.context_map:DefaultDict[str, ChatContext] = defaultdict(lambda:ChatContext())

    def get_context(self, context_id:str)->ChatContext:
        return self.context_map.get(context_id)
    
    def add_chat_history(self, context_id:str, model_name:str, message:ChatMessage):
        self.context_map[context_id].chat_history_of[model_name].append(message)
    
    def update_context(self, context_id:str, model_name:str, message:str):
        self.add_chat_history(context_id, model_name, ChatMessage("user", message))
    
    def reset_context(self, context_id:str):
        self.context_map[context_id] = ChatContext()
    
    def get_conversation_id(self, context_id:str, model_name:str):
        return self.context_map[context_id].conversation_id_of[model_name]
    
    def get_parent_id(self, context_id:str, model_name:str):
        return self.context_map[context_id].parent_id_of[model_name]
    
    def set_conversation_id(self, context_id:str, model_name:str, conversation_id:str):
        self.context_map[context_id].conversation_id_of[model_name] = conversation_id

    def set_parent_id(self, context_id:str, model_name:str, parent_id:str):
        self.context_map[context_id].parent_id_of[model_name] = parent_id
    
    def set_model_name(self, context_id:str, model_name:str):
        self.context_map[context_id].global_model = model_name
    
    def get_model_name(self, context_id:str):
        return self.context_map[context_id].global_model

context_manager = ContextManager()


