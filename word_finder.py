import parser_lib
from check_lib import check_the_file_for_some_parameters


def output_result_of_parsing(result_of_parsing, item_count=5):
    """
    parsing result output
    """    

    firstN = result_of_parsing[:item_count]
    
    for item in firstN:
        print(f"{item[0]}={item[1]}")


if __name__ == "__main__":
    
    parser = parser_lib.init_parser()
    args = parser.parse_args()
    
    message = check_the_file_for_some_parameters(file_name=args.file_name)
    if message:
        
        print(message)        
    else:
        
        result_of_parsing = parser_lib.parse_file(args.file_name)
        output_result_of_parsing(result_of_parsing)