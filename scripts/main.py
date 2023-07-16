#!/usr/bin/env python3.10

from pptx import Presentation
from report_generator import ReportGenerator
from data_handler import DataHandler
from typing import List 
import logging, timeit
import sys


FILE_PATH = "data/data.json" #TODO get file_path as argument
POSSIBLE_TYPES = ["title", "text", "list", "picture", "plot"]
POSSIBLE_KEYS = ["type", "title", "content", "configuration"]

def main():
    '''
    Takes a valid .json file as an argument and uses it to generate a .pptx report.
    '''

    start = timeit.default_timer()
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    if sys.version_info[0] != 3:
        raise Exception("Python version 3 is needed to run this program.")
    
    logging.info('Program started')


    raw_data = DataHandler(FILE_PATH)
    slides_data: List[dict] = raw_data.get_data_from_file()

    generator = ReportGenerator(POSSIBLE_TYPES, POSSIBLE_KEYS)
    generator.generate_report(slides_data)


    end = timeit.default_timer()
    logging.info('Finished in: {} seconds.'.format(end-start))



##################################################################

if __name__ == '__main__':
    main()