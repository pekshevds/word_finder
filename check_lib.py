from os import path
import config


__all__ = ['check_the_file_for_some_parameters']


def encoding_of_this_file_is_utf_8(file_name):
    
    with open(file_name, mode='r', encoding='utf-8') as file:
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
        file = open(file_name, mode='rb', encoding='utf-8')
    except ValueError:
        return True

    file.close()
    return False


def check_the_file_for_some_parameters(file_name):
    """
    check the file for some params (existence, content type, encoding end etc)
    """    

    if not path.exists(file_name) or not path.isfile(file_name):
        return 'this file does not exist or is not a file'
    
    if not this_file_is_text(file_name):
        return 'this file is not a text file'
    
    if not encoding_of_this_file_is_utf_8(file_name):
        return 'the encoding of this file is not utf-8'

    if not (1 <= path.getsize(filename=file_name) < config.MAX_FILE_LENGTH):
        return f'the size of this file must be between 1 byte and {config.MAX_FILE_LENGTH//1024}Kb'

    return ''