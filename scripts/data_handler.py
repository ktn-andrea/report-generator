#!/usr/bin/env python3.10

import json

class DataHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_path(self):
        return self.file_path
    
    def set_file_path(self, f):
        self._filepath = f


    def get_data_from_file(self):
        f = open(self.get_file_path(), "r")
        data = json.load(f)
        keys, values = zip(*data.items())

        if self.is_file_valid(keys, values) == True:
            return self.get_slides_data(values)


    def is_file_valid(self, keys, values):
        '''
        Checks if the format is appropriate. This application generates one report, therefore there should be only one "presentation" key and one corresponding value (list).
        '''
        if len(keys) == 1 and keys[0] == "presentation" and len(values) == 1:
            return True


    def get_slides_data(self, values):
        slides_data = []
        for item in values:
            num_of_slides = 0
            for slide_content in item:
                #print(slide_content)
                num_of_slides += 1
                slides_data.append(slide_content)
                #print(num_of_slides)
        return slides_data


