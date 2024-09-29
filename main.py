#!/bin/env python

from src.readers import *
from src.plotters import *

if __name__ == "__main__":
    
    raven_obj = RAVEN_Reader()
    arc_obj = ARC_Reader()

    data = arc_obj.train_dataset[1]
    plot_arc_data(data)