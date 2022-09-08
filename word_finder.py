import argparse
from os import path

MAX_FILE_LENGTH = 64

def encoding_of_this_file_is_utf_8(file_name):
    """
    check encoding some file
    """

    return True


def this_file_is_text(file_name):
    """
    check if file is text
    """
    
    return True


def check_file(file_name):
    """
    check the file for some params (existence, content type, encoding end etc)
    """    

    return True, 'ok'


def delete_some_simbols_from_word(word):
    """
    cleaning the word from unnecessary characters
    """

    return "".join(ch for ch in word if not ch in """!@#$%^&*()/"*-+\|?><.,№;%:[]}{='""").lower()


def split_some_text_into_words(text):
    """
    split some text into words
    """
    return text.split(' ')


def parse_file(file_name):
    """
    splits file data into parts, removes unnecessary characters
     and sorts by frequency of occurrence
    """    

    return []
   

def init_parser():
    """
    parser initialization
    """
    
    parser = argparse.ArgumentParser(description="word finder")    
    parser.add_argument('file_name', type=str, help='name of file', default='text.txt')    
    return parser


def output_result_of_parsing(result_of_parsing, item_count=5):
    """
    parsing result output
    """    

    firstN = result_of_parsing[:item_count]
    
    for item in firstN:
        print(f"{item[0]}={item[1]}")


if __name__ == "__main__":
    
    parser = init_parser()
    args = parser.parse_args()
    
    success, message = check_file(file_name=args.file_name)
    if success:
        
        result_of_parsing = parse_file(args.file_name)
        output_result_of_parsing(result_of_parsing)
    else:
        
        print(message)