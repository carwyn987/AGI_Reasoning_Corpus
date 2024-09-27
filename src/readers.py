import os
import json
import numpy as np
import matplotlib.pyplot as plt

def read_text_file(filename: str):
    with open(filename, 'r') as file_handle:
        text = file_handle.read()
    return text

def read_json_file(filename: str):
    with open(filename, 'r') as file_handle:
       data = json.load(file_handle) 
    return data

def read_npz_file(filename: str):
    return np.load(filename)

def extract_npz_data(obj):
    keys = list(obj.keys())
    return {key: obj[key] for key in keys}

def plot_npz_image(image):
    fig, axs = plt.subplots(4, 4, figsize=(16, 16))
    for i in range(16):
        axs[i // 4, i % 4].imshow(image[i, :, :])
        axs[i // 4, i % 4].set_title(f'Channel {i}')
    plt.show()
    
class Reader:
    def __init__(self):
        self.base_data_dir = ""
        self.sub_data_dirs = []

    def get_all_sub_data_dirs(self, intermediate_dir=''):
        data_dir = os.path.join(self.data_directory, intermediate_dir)

        if not os.path.exists(data_dir):
            raise FileNotFoundError(f"The data directory '{data_dir}' does not exist.")

        self.sub_data_dirs = [os.path.join(data_dir, d) for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]

class ARC_Reader(Reader):
    def __init__(self):
        Reader.__init__(self)

        self.data_directory = os.path.join(os.environ.get('ARC_AGI_BASE'),'data')

class RAVEN_Reader(Reader):
    def __init__(self):
        Reader.__init__(self)

        self.data_directory = os.path.join(os.environ.get('RAVEN_BASE'),'data')