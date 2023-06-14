import torch
from torch.utils.data import Dataset

class AudioDataset(Dataset):
    def __init__(self, data, labels, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        audio = self.data[index]
        label = self.labels[index]
        
        if self.transform:
            audio = self.transform(audio)
        
        return audio, label
