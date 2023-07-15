#!/usr/bin/env python3.10

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.chart.data import XyChartData
from pptx.enum.chart import XL_CHART_TYPE
from typing import List
import numpy as np
from typing import NewType


'''
0: Title Slide
1: Title and Content
'''
SLIDE_LAYOUT_MODE = 0 



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
                    if slide_type == "title":
                        print("Generating title slide")
                        SLIDE_LAYOUT_MODE = 0
                        Title_Layout = self.report.slide_layouts[SLIDE_LAYOUT_MODE]
                        new_slide = self.report.slides.add_slide(Title_Layout)
                        self.generate_title_slide(raw_slide_data, new_slide)
                    else: 
                        SLIDE_LAYOUT_MODE = 1
                        Content_Layout = self.report.slide_layouts[SLIDE_LAYOUT_MODE]
                        new_slide = self.report.slides.add_slide(Content_Layout)
                        if slide_type == "text":
                            print("Generating text slide")
                            self.generate_text_slide(raw_slide_data, new_slide)
                        elif slide_type == "list":
                            print("Generating list slide")
                            self.generate_list_slide(raw_slide_data, new_slide)
                        elif slide_type == "picture":
                            print("Generating picture slide")
                            self.generate_picture_slide(raw_slide_data, new_slide)
                        elif slide_type == "plot":
                            print("Generating plot slide")
                            self.generate_plot_slide(raw_slide_data, new_slide)

        self.report.save("Test.pptx")
    

    def generate_title_slide(self, slide_data: dict, slide: type[Presentation]) -> None:
        print("Creating Title Slide....")
        print(slide_data)

        slide.shapes.title.text = slide_data.get("title")
        slide.placeholders[1].text = slide_data.get("content")
        
        print("Title Slide Done")


    def generate_text_slide(self, slide_data: dict, slide: type[Presentation]) -> None:
        print("Creating Text Slide....")
        print(slide_data)
        slide.shapes.title.text = slide_data.get("title")
        #slide.placeholders[1].text = slide_data.get("content")
        
        textbox = slide.shapes.add_textbox(Inches(1), Inches(1.5),Inches(3), Inches(1))
        textbox.text = slide_data.get("content")
        
        print("Text Slide Done")


    def generate_list_slide(self, slide_data: dict, slide: type[Presentation]) -> None:
        print("Creating List Slide....")
        print(slide_data)
        slide.shapes.title.text = slide_data.get("title")

        textbox = slide.shapes.add_textbox(Inches(1), Inches(1.5),Inches(3), Inches(1))
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


    def generate_picture_slide(self, slide_data: dict, slide: type[Presentation]) -> None:
        print("Creating Picture Slide....")
        print(slide_data)
        slide.shapes.title.text = slide_data.get("title")

        left = top = Inches(1.8) 
        slide.shapes.add_picture(slide_data.get("content"), left, top)

        print("Picture Slide Done")


    def generate_plot_slide(self, slide_data: dict, slide: type[Presentation]) -> None:
        print("Creating Plot Slide....")
        print(slide_data)
        slide.shapes.title.text = slide_data.get("title")

        plot_file = slide_data.get('content').replace('.dat', '.csv')
        arr = np.loadtxt(plot_file, delimiter=';', dtype = float)
        print(arr)

        chart_data = XyChartData()

        series = chart_data.add_series('Series')
        series.has_title = False
        
        for a in arr:
            series.add_data_point(a[0], a[1])
            print(a[0], a[1])
        
        x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
        c = slide.shapes.add_chart(XL_CHART_TYPE.XY_SCATTER, x, y, cx, cy, chart_data).chart
        
        axis_labels: dict = slide_data.get("configuration")
        category_axis_title = c.category_axis.axis_title
        category_axis_title.text_frame.text = axis_labels.get("x-label")
        value_axis_title = c.value_axis.axis_title
        value_axis_title.text_frame.text = axis_labels.get("y-label")
 
        print("Plot Slide Done")
