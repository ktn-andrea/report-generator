#!/usr/bin/env python3.10

from pptx import Presentation
from data_handler import DataHandler
from typing import List

SLIDE_LAYOUT_MODE = 0 
'''
0: Title (Title Slide)
1: Text (Title and Content)
2: List (Title and Content)
3: Picture (Blank? , 6)
4: Plot (Blank? , 6)
'''

""" Slide types: 
0 ->  title and subtitle
1 ->  title and content
2 ->  section header
3 ->  two content
4 ->  Comparison
5 ->  Title only 
6 ->  Blank
7 ->  Content with caption
8 ->  Pic with caption
"""

class ReportGenerator():
    def __init__(self, possible_types: List, possible_keys: List):
        report = Presentation()
        self.possible_types = possible_types
        self.possible_keys = possible_keys


    def keys_validation(self, keys):
        for key in keys:
            if key not in self.possible_keys:
                return False
        return True

    def generate_report(self, data: List[dict]):
        for slide in data:
            are_keys_valid = self.keys_validation(slide.keys())
            if are_keys_valid == False:
                print("Error: invalid key found")

            else:
                slide_type = slide["type"].lower()
                #print(slide)
                if slide_type not in self.possible_types:
                    print("Error: slide type not supported")
                else:
                    if slide_type == "title":
                        pass
                    elif slide_type == "text":
                        pass
                    elif slide_type == "list":
                        pass
                    elif slide_type == "picture":
                        pass
                    elif slide_type == "plot":
                        pass
    

    def generate_title_slide():
        pass

    def generate_text_slide():
        pass

    def generate_list_slide():
        pass

    def generate_picture_slide():
        pass

    def generate_plot_slide():
        pass
