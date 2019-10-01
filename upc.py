#!/usr/bin/env python3
"""Retrieves UPC numbers from internet"""
import os
import sys
from multiprocessing import Pool
from itertools import repeat

def upc(f):
    """Gets UPC from internet and passess it to a callback function.
    
    Args: 
        f: callback function receiving UPC in string form.

    """
    upc = os.popen('upc').read().rstrip('\n')
    f(upc)

def main(count):
    """Prints a listing of UPCs.
    
    Args: 
        count: number of upcs to print.
    """
    with Pool() as pool:
        pool.map(upc, repeat(print, count))

if __name__ == "__main__":
    count = 1
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    
    main(count)
    
