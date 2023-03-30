class ChatMessage:
    speaker:str=None
    message:str=None
    def __init__(self, speaker:str, message:str):
        self.speaker = speaker
        self.message = message