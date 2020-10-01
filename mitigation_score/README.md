# Mitigation Score

Translation of Jon Cohen's COVID-19 mitigation score calculations within Pointillist/QUILT into a Python script. Tested with Python 3.8.3.

## Setup:

Enter the topmost directory of the project, then create a virtual environment.
* On Windows:
    * `python -m venv venv`
    * `venv\Scripts\activate`
* On MacOS/Linux:
    * `python -m venv venv`
    * `source venv/bin/activate`  
  
Install the requirements.  
`pip install -r requirements.txt`

Leave the virtual environment.  
`deactivate`

## How to run:

Enter virtual environment.
* On Windows:
    * `venv\Scripts\activate`
* On MacOS/Linux:
    * `source venv/bin/activate`   

Enter desired settings into `config.py` file.  

Run the script.  
`python calculate-mitigation-score.py`

When finished:  
`deactivate`