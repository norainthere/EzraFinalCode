import torch

class AudioAnalyzer:
    def __init__(self):
        self.model = torch.load('models/model.ckpt')
        
    def analyze(self, audio):
        # Preprocess the audio
        audio = self.transform(audio)

        # Apply the model
        analysis = self.model(audio)

        return analysis
