#!/usr/bin/env python3.10

import json
from typing import List
from jsonschema import validate
import jsonschema
import logging
logger = logging.getLogger(__name__)

class DataHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_path(self):
        return self.file_path
    
    def set_file_path(self, f):
        self._filepath = f


    def get_data_from_file(self) -> List[dict]:
        '''
        Returns the slides data (value of "presentation" key) from json file if the data is valid according to the schema.
        '''
        with open(self.get_file_path(), 'r') as f:
            data = json.load(f)

        keys, values = zip(*data.items())

        isvalid: bool = self.validateJson(data)

        if isvalid == True:
            logging.info("Json file is valid according to the schema.")
            return self.get_slides_data(values)
        else:
            logging.fatal("Json file is not valid according to the schema.")
            exit()


    def validateJson(self, jsondata: dict) -> bool:
        '''
        Returns whether the json data given as argument is valid according to the schema file.
        '''
        with open('./data/schema.json', 'r') as file:
            reportschema = json.load(file)

        try:
            validate(instance=jsondata, schema=reportschema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    
    def get_slides_data(self, values) -> List[dict]:
        '''
        Collects the (list) value of the "presentation" key, which contains the necessary data for creating slides.
        '''
        slides_data = []
        for item in values:
            for slide_content in item:
                slides_data.append(slide_content)
        logging.info("Extracted slides data")
        return slides_data
        