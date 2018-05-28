import json
import pandas as pd
import os

def set_home_dir():
    cur_dir = os.getcwd()
    sep = '/notebooks'
    rest = cur_dir.split(sep, 1)[0]
    os.chdir(rest)

def load_yle_fi():
	#load Yle finnish articles:
	yle_fi_dict = None
	with open("data/yle_finnish_articles_mentioning_russia.json",  encoding='utf-8') as json_data:
	    yle_fi_dict= json.load(json_data)
	    json_data.close()

	yle_fi_data = pd.DataFrame.from_dict(yle_fi_dict['results']['docs'])

	return yle_fi_data
