from os import path
from .config import MAX_FILE_LENGTH_Kb


__all__ = ['check_the_file_for_some_parameters']


def _encoding_of_this_file_is_utf_8(file_name):
    
    with open(file_name, mode='r', encoding='utf-8') as file:
        try:
            file.read()
        except UnicodeDecodeError:
            return False

    return True


def _this_file_is_text(file_name):
    """
    check if file is text
    """
    
    try:
        with open(file_name, mode='rb', encoding='utf-8') as file:
            pass
    except ValueError:
        return True

    return False


def check_the_file_for_some_parameters(file_name):
    """
    check the file for some params (existence, content type, encoding end etc)
    """    

    if not path.exists(file_name) or not path.isfile(file_name):
        return 'this file does not exist or is not a file'
    
    if not _this_file_is_text(file_name):
        return 'this file is not a text file'
    
    if not _encoding_of_this_file_is_utf_8(file_name):
        return 'the encoding of this file is not utf-8'

    if not (1 <= path.getsize(filename=file_name) < MAX_FILE_LENGTH_Kb):
        return f'the size of this file must be between 1 byte and {MAX_FILE_LENGTH_Kb//1024}Kb'

    return ''