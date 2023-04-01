from discord import Interaction

class MessageSender:
    def __init__(self):
        self.char_limit = 1900

    async def send(self, interaction:Interaction, message:str):
        chunks = [message[i:i + self.char_limit] for i in range(0, len(message), self.char_limit)]
        for chunk in chunks:
            await interaction.followup.send(chunk)


message_sender = MessageSender()