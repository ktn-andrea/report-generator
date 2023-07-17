#!/usr/bin/env python3.9

import sys, logging, timeit, pathlib
from typing import List 
from report_generator import ReportGenerator
from data_handler import DataHandler
from report_generator import ReportGenerator


POSSIBLE_TYPES = ["title", "text", "list", "picture", "plot"]
POSSIBLE_KEYS = ["type", "title", "content", "configuration"]

def main():
    '''
    Takes a valid .json file as an argument and uses it to generate a .pptx report.
    '''
    FILE_PATH = pathlib.Path(sys.argv[1])

    raw_data: type[DataHandler] = DataHandler(FILE_PATH)
    slides_data: List[dict] = raw_data.get_data_from_file()

    generator: type[ReportGenerator] = ReportGenerator(POSSIBLE_TYPES, POSSIBLE_KEYS)
    generator.generate_report(slides_data)
    generator.save_output(generator)

    end: float = timeit.default_timer()
    logging.info('Finished in: {} seconds.'.format(end-start))


##################################################################

if __name__ == '__main__':
    '''
    Check Python version and argument - only one .json file path should be provided.
    '''

    logging.basicConfig(filename='./data/log.txt', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    if sys.version_info[0] != 3:
        logging.error("Python version 3 is needed to run this program.")
    
    if len(sys.argv) == 2:
        arg_extension = pathlib.Path(sys.argv[1]).suffix
        if arg_extension == ".json":
            logging.info('Starting application')
            start: float = timeit.default_timer()
            main()
        else:
            logging.fatal("Error: argument is not a json file.")
            raise Exception("The argument should have a .json extension.")
    else:
        logging.fatal("Error: one argument should be given.")
        raise Exception("Please provide one input .json file as an argument.")
    
        