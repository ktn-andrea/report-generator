# 📃 Report generator

An application that generates a report in pptx format based on a json configuration file.\
Five slide types are supported: Title, Text, List, Picture and Plot slide.


🔌 Getting Started
-------------------

- Python version used for this project: 3.9.12
- Make sure $PYTHONPATH is set correctly on your machine
- Consider using a virtual environment
- All files that are required for the report generation *(.png, .csv)* should be in the */data/* folder - otherwise, the slide will not be created
- Sample data is provided in */data/* folder
- It is required for the json file to be valid, *./data/schema.json* is used for validation
- Use *./data/data.json* as a template for configuration
- Only one argument (path to *.json*) should be passed

💻 Using the Project
-------------------
1. Clone the repository:\
`git clone https://github.com/ktn-andrea/report-generator.git`

1. Step into project folder:\
`cd ./report-generator/`

1. Use Virtual Environment *(Recommended)*:\
`pip install virtualenv`\
`python<version> -m venv env`\
Activate the environment:\
`source env/bin/activate` (Linux)\
`env/Scripts/Activate.ps1` (PowerShell)\

1. Install the required packages with pip:\
`pip install -r requirements.txt`

1. Run main.py script with the location of a .json configuration file as argument:\
`python ./scripts/main.py ./data/data.json`

The generated report will be in **/data/output.pptx**

💼 Project Organization
------------------------

    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    ├── scripts
    │   ├── main.py
    │   ├── data_handler.py
    │   └── report_generator.py
    ├── data
    │   ├── picture.png
    │   ├── sample.csv
    │   ├── data.json
    │   └── schema.json
