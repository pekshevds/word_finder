import argparse
from collections import Counter
from .word_lib import get_cleared_words


def init_parser():
    """
    parser initialization
    """
    
    parser = argparse.ArgumentParser(description="word finder")    
    parser.add_argument('file_name', type=str, help='name of file', default='text.txt') 
    parser.add_argument('--count', type=int, help='records count', default=5)    
    return parser


def parse_file(file_name):
    """
    splits file data into parts, removes unnecessary characters
     and sorts by frequency of occurrence
    """    

    with open(file_name, mode='r', encoding='utf-8') as file:
        rating = Counter(get_cleared_words(file.read()))
    
    
    return rating