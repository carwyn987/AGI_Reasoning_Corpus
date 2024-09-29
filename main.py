#!/bin/env python

import argparse

from src.readers import *
from src.plotters import *

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Load and plot datasets')
    parser.add_argument('--dataset', nargs='+', choices=['raven', 'arc'], default=['raven', 'arc'],
                        help='Specify which dataset(s) to load (default: all)')
    parser.add_argument('--show', action='store_true', help='Display the plots (default: False)')

    args = parser.parse_args()

    if 'raven' in args.dataset:
        raven_obj = RAVEN_Reader()
        if args.show:
            raven_obj.show()


    if 'arc' in args.dataset:
        arc_obj = ARC_Reader()
        if args.show:
            arc_obj.show()