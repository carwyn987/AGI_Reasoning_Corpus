import os
import json
import numpy as np
from torch.utils.data import Dataset

def read_npz_file(filename: str):
    return np.load(filename)

def extract_npz_data(obj):
    keys = list(obj.keys())
    return {key: obj[key] for key in keys}

class CustomDataset(Dataset):
    def __init__(self):
        self.files = []

    def __len__(self):
        raise NotImplementedError()

    def __getitem__(self):
        raise NotImplementedError() 
    
class RAVEN_Dataset(CustomDataset):
    def __init__(self, sub_data_dirs):
        CustomDataset.__init__(self)

        # Walk the folder files
        for data_dir in sub_data_dirs:
            for root, dirs, files in os.walk(data_dir):
                for file in files:
                    if file.endswith('.npz'):
                        self.files.append(os.path.join(root, file))
                        
    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        try:
            npz_file = read_npz_file(self.files[idx])
            npz_data = extract_npz_data(npz_file)
            label = npz_data["target"]
            example_set = npz_data['image'][:8]
            candidates = npz_data['image'][8:]
                      
            assert label >= 0 and label < 8
            assert len(example_set) == 8
            assert len(candidates) == 8
        except:
            print("Error loading RAVEN sample ... skipping")

        return {'example_set': example_set, 'candidates': candidates, 'label': label}
    
class ARC_Dataset(CustomDataset):
    def __init__(self, data_dir):
        CustomDataset.__init__(self)

        # Walk the folder files
        for root, dirs, files in os.walk(data_dir):
            for file in files:
                if file.endswith('.json'):
                    self.files.append(os.path.join(root, file))

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        try:
            with open(self.files[idx], 'r') as f:
                data = json.load(f)

        except:
            print("Error loading ARC sample ... skipping")

        return data