import os
import json
import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass, field

from src.datasets import ARC_Dataset, RAVEN_Dataset
from src.plotters import *

def read_text_file(filename: str):
    with open(filename, 'r') as file_handle:
        text = file_handle.read()
    return text

def read_json_file(filename: str):
    with open(filename, 'r') as file_handle:
       data = json.load(file_handle) 
    return data

@dataclass
class Reader:
    def __init__(self):
        self.base_data_dir = ""
        self.sub_data_dirs = []

    def get_all_sub_data_dirs(self, intermediate_dir=''):
        data_dir = os.path.join(self.data_directory, intermediate_dir)

        if not os.path.exists(data_dir):
            raise FileNotFoundError(f"The data directory '{data_dir}' does not exist.")

        self.sub_data_dirs = [os.path.join(data_dir, d) for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]

    def load(self):
       raise NotImplementedError() 

class ARC_Reader(Reader):
    def __init__(self):
        Reader.__init__(self)

        self.data_directory = os.path.join(os.environ.get('ARC_AGI_BASE'),'data')
        self.train_directory = os.path.join(self.data_directory, 'training')
        self.eval_directory = os.path.join(self.data_directory, 'evaluation')
        self.load()

    def load(self):
        self.train_dataset = ARC_Dataset(self.train_directory)
        self.eval_dataset = ARC_Dataset(self.eval_directory)

    def show(self, idx=0):
        try:
            plot_arc_data(self.train_dataset[idx])
        except:
            raise ModuleNotFoundError()

class RAVEN_Reader(Reader):
    def __init__(self):
        Reader.__init__(self)

        self.data_directory = os.path.join(os.environ.get('RAVEN_BASE'),'data')
        self.load()

    def load(self):
        self.get_all_sub_data_dirs(intermediate_dir='')
        self.dataset = RAVEN_Dataset(self.sub_data_dirs)

    def show(self, idx=0):
        try:
            plot_raven_image(self.dataset[idx])
        except:
            raise ModuleNotFoundError()