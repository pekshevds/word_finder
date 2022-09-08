import argparse
from os import path

MAX_FILE_LENGTH = 64*1024

def encoding_of_this_file_is_utf_8(file_name):
    """
    check encoding some file
    """

    file = open(file_name, mode='r', encoding='utf-8')
    try:
        file.read()
    except UnicodeDecodeError:
        return False

    return True


def this_file_is_text(file_name):
    """
    check if file is text
    """
    
    try:
        open(file_name, mode='rb', encoding='utf-8')
    except ValueError:
        return True

    return False


def check_file(file_name):
    """
    check the file for some params (existence, content type, encoding end etc)
    """    

    if not path.exists(file_name) or not path.isfile(file_name):
        return False, 'this file does not exist or is not a file'
    
    if not this_file_is_text(file_name):
        return False, 'this file is not a text file'
    
    if not encoding_of_this_file_is_utf_8(file_name):
        return False, 'the encoding of this file is not utf-8'

    if not (1 <= path.getsize(filename=file_name) < MAX_FILE_LENGTH):
        return False, f'the size of this file must be between 1 byte and {MAX_FILE_LENGTH//1024}Kb'

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


def get_cleared_words(text):
    """
    split text into words and cleare them
    """

    dirty_words = split_some_text_into_words(text)
    return list(map(delete_some_simbols_from_word, dirty_words))


def parse_file(file_name):
    """
    splits file data into parts, removes unnecessary characters
     and sorts by frequency of occurrence
    """    

    file = open(file_name, mode='r', encoding='utf-8')
    words = get_cleared_words(file.read())

    rating = {}
    for word in words:
        
        if rating.get(word, 0) == 0:
            rating[word] = 1
        else:
            rating[word] += 1
    
    return sorted(rating.items(), reverse= True, key=lambda x: x[1])
   

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