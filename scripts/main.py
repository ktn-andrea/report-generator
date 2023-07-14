#!/usr/bin/env python3.10

from pptx import Presentation
from report_generator import ReportGenerator
from data_handler import DataHandler
from typing import List 


FILE_PATH = "scripts/data.json"
POSSIBLE_TYPES = ["title", "text", "list", "picture", "plot"]
POSSIBLE_KEYS = ["type", "title", "content", "configuration"]

def main():

    raw_data = DataHandler(FILE_PATH)
    slides_data: List[dict] = raw_data.get_data_from_file()

    #print(slides_data)

    generator = ReportGenerator(POSSIBLE_TYPES, POSSIBLE_KEYS)
    generator.generate_report(slides_data)



main()