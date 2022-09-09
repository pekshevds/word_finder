from word_finder.parser_lib import init_parser, parse_file
from word_finder.check_lib import check_the_file_for_some_parameters


def output_result_of_parsing(result_of_parsing, count=5):
    """
    parsing result output
    """    

    for word, frequency in result_of_parsing.most_common(count):
        print(f"{word}={frequency}")


if __name__ == "__main__":
    
    parser = init_parser()
    args = parser.parse_args()
    
    message = check_the_file_for_some_parameters(file_name=args.file_name)
    if message:
        
        print(message)        
    else:
        
        result_of_parsing = parse_file(args.file_name)
        output_result_of_parsing(result_of_parsing, args.count)