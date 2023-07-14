#!/usr/bin/env python3.10

from pptx import Presentation
from pptx.util import Inches, Pt
from data_handler import DataHandler
from typing import List

SLIDE_LAYOUT_MODE = 0 
'''
0: Title (Title Slide, 0)
1: Text (Title and Content, 1)
2: List (Title and Content, 1)
3: Picture (Title and Content, 1)
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
    def __init__(self, possible_types: List, possible_keys: List) -> None:
        self.report = Presentation()
        self.possible_types: List = possible_types
        self.possible_keys: List = possible_keys


    def keys_validation(self, keys: dict.keys) -> bool:
        print(type(keys))
        for key in keys:
            if key not in self.possible_keys:
                return False
        return True

    def generate_report(self, data: List[dict]):
        for raw_slide_data in data:
            are_keys_valid: bool = self.keys_validation(raw_slide_data.keys())
            if are_keys_valid == False:
                print("Error: invalid key found")

            else:
                slide_type = raw_slide_data["type"].lower()
                #print(slide)
                if slide_type not in self.possible_types:
                    print("Error: slide type not supported")
                else:
                    if slide_type == "title": #DONE
                        print("Generating title slide")
                        SLIDE_LAYOUT_MODE = 0
                        self.generate_title_slide(raw_slide_data, SLIDE_LAYOUT_MODE)
                    elif slide_type == "text": #DONE
                        print("Generating text slide")
                        SLIDE_LAYOUT_MODE = 1
                        self.generate_text_slide(raw_slide_data, SLIDE_LAYOUT_MODE)
                    elif slide_type == "list":  #DONE
                        print("Generating list slide")
                        SLIDE_LAYOUT_MODE = 1  
                        self.generate_list_slide(raw_slide_data, SLIDE_LAYOUT_MODE)
                    elif slide_type == "picture":  #DONE
                        print("Generating picture slide")
                        SLIDE_LAYOUT_MODE = 1
                        self.generate_picture_slide(raw_slide_data, SLIDE_LAYOUT_MODE)
                    elif slide_type == "plot":
                        print("Generating plot slide")
                        SLIDE_LAYOUT_MODE = 6
                        self.generate_plot_slide(raw_slide_data, SLIDE_LAYOUT_MODE)

        self.report.save("Test.pptx")
    

    def generate_title_slide(self, slide_data: dict, slide_layout: int) -> None:
        print("Creating Title Slide....")
        print(slide_data)
        Title_Layout = self.report.slide_layouts[slide_layout]
        new_slide = self.report.slides.add_slide(Title_Layout)
        new_slide.shapes.title.text = slide_data.get("title")
        new_slide.placeholders[1].text = slide_data.get("content")
        
        print("Title Slide Done")

    def generate_text_slide(self, slide_data: dict, slide_layout: int) -> None:
        print("Creating Text Slide....")
        print(slide_data)
        Text_Layout = self.report.slide_layouts[slide_layout]
        new_slide = self.report.slides.add_slide(Text_Layout)
        new_slide.shapes.title.text = slide_data.get("title")
        
        textbox = new_slide.shapes.add_textbox(Inches(1), Inches(1.5),Inches(3), Inches(1))
        textbox.text = slide_data.get("content")
        #textframe = textbox.text_frame
        #textframe.text = slide_data.get("content")
        #paragraph = textframe.add_paragraph()
        #paragraph.text = slide_data.get("content")
        
        print("Text Slide Done")

    def generate_list_slide(self, slide_data: dict, slide_layout: int) -> None:
        print("Creating List Slide....")
        print(slide_data)
        List_Layout = self.report.slide_layouts[slide_layout]
        new_slide = self.report.slides.add_slide(List_Layout)
        new_slide.shapes.title.text = slide_data.get("title")

        textbox = new_slide.shapes.add_textbox(Inches(1), Inches(1.5),Inches(3), Inches(1))
        list_content: list = slide_data.get("content")
        textframe = textbox.text_frame
        for level_data in list_content:
            level_num: int = int(level_data.get("level"))
            paragraph = textframe.add_paragraph()
            if level_num == 1:
                paragraph.text = '- ' + str(level_data.get("text"))
                paragraph.font.size = Pt(30)
            elif level_num == 2:
                paragraph.text = '   ' + str(level_data.get("text"))
                paragraph.font.size = Pt(20)
            else:
                paragraph.text = '     ' + str(level_data.get("text"))
                paragraph.font.size = Pt(10)

        print("List Slide Done")

    def generate_picture_slide(self, slide_data: dict, slide_layout: int) -> None:
        print("Creating Picture Slide....")
        print(slide_data)
        Picture_Layout = self.report.slide_layouts[slide_layout]
        new_slide = self.report.slides.add_slide(Picture_Layout)
        new_slide.shapes.title.text = slide_data.get("title")

        left = top = Inches(1.8) 
        new_slide.shapes.add_picture(slide_data.get("content"), left, top)

        print("Picture Slide Done")

    def generate_plot_slide(self, slide_data: dict, slide_layout: int) -> None:
        print(slide_data)
