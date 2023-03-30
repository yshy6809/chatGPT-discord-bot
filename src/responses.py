from src import personas
from asgiref.sync import sync_to_async
from src.context.context import context_manager

async def official_handle_response(message, client) -> str:
    return await sync_to_async(client.chatbot.ask)(message)

async def unofficial_handle_response(channel_id:int, model_name:str, message:str, client) -> str:
    conversation_id = context_manager.get_conversation_id(channel_id, model_name)
    parent_id = context_manager.get_parent_id(channel_id, model_name)
    async for response in client.chatbot.ask(message, conversation_id, parent_id):
        #responseMessage = response["message"]
        final_response = response
    client.chatbot.conversation_id = None
    client.chatbot.conversation_parent_id = None
    context_manager.set_conversation_id(channel_id, model_name, final_response["conversation_id"]) 
    context_manager.set_parent_id(channel_id, model_name, final_response["parent_id"])
    return final_response["message"]

# resets conversation and asks chatGPT the prompt for a persona
async def switch_persona(persona, client) -> None:
    if client.chat_model ==  "UNOFFICIAL":
        client.chatbot.reset_chat()
        async for response in client.chatbot.ask(personas.PERSONAS.get(persona)):
            pass

    elif client.chat_model == "OFFICIAL":
        client.chatbot.reset()
        await sync_to_async(client.chatbot.ask)(personas.PERSONAS.get(persona))
