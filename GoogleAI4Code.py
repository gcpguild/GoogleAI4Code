"""
Google AI for Code.py  
Python : Parse for parase the JSON and predict
_____________________________________________________________________________
Project contact: Google AI for Code API, Nature Labs, Kyndryl
Email: gcpguild@gmail.com
Project : Python API for Google AI for Code

The goal of this application is to understand the relationship between code and comments in Python notebooks. You are challenged to reconstruct the order of markdown cells in a given notebook based on the order of the code cells, demonstrating comprehension of which natural language references which code.
Context
---------
Research teams across Google and Alphabet are exploring new ways that machine learning can assist software developers, and want to rally more members of the developer community to help explore this area too. Python notebooks provide a unique learning opportunity, because unlike a lot of standard source code, notebooks often follow narrative format, with comment cells implemented in markdown that explain a programmer's intentions for corresponding code cells. An understanding of the relationships between code and markdown could lend to fresh improvements across many aspects of AI-assisted development, such as the construction of better data filtering and preprocessing pipelines for model training, or automatic assessments of a notebook's readability.
We have assembled a dataset of approximately 160,000 public Python notebooks from Kaggle and have teamed up with X, the moonshot factory to design a competition that challenges participants to use this dataset of published notebooks to build creative techniques aimed at better understanding the relationship between comment cells and code cells.
This program is written in Python Language

Created for Lab purposes with regulations of Nature Labs

The dataset for this competition comprises about 160,000 Jupyter notebooks published by the Kaggle community. Jupyter notebooks are the tool of choice for many data scientists for their ability to tell a narrative with both code and natural language. These two types of discourse are contained within cells of the notebook, and we refer to these cells as either code cells or markdown cells (markdown being the text formatting language used by Jupyter).

Your task is to predict the correct ordering of the cells in a given notebook whose markdown cells have been shuffled.

The notebooks in this dataset have been selected and processed to ensure their suitability for the competition task. All notebooks:

Have been published publicly on Kaggle under the Apache 2.0 open source license.
Represent the most recently published version of the notebook.
Contain at least one code cell and at least one markdown cell.
Have code written in the Python language.
Have had empty cells removed.
This is a code competition, in which you will submit a model or code that will be run against a future test set:

The first-stage test set contains notebooks from an approximately 90-day historical window of time.
The second-stage test set will contain a similar number of notebooks, collected from a future 90-day window of time. This is necessary to prevent models from looking up the order of existing public notebooks. The selection criteria for second-stage notebooks will be monitored for competition fairness purposes. For example, it will exclude competition participants' own notebooks.
Training Data
train/ - A folder comprising about 140,000 JSON files with the filenames corresponding to the id field in the csv files. Each file contains the code and markdown cells of a Kaggle notebook. The code cells are in their original (correct) order. The markdown cells have been shuffled and placed after the code cells.
train_orders.csv - Gives the correct order of the cells for each notebook in the train/ folder.
id - The notebook in file {id}.json.
cell_order - A space delimited list of the correct cell ordering given in terms of the order in {id}.json.
train_ancestors.csv - On Kaggle, a user may "fork" (that is, copy) the notebook of another user to create their own version. This file contains the forking history of notebooks in the training set. Note: There is no corresponding file for the test set.
ancestor_id - Identifies sets of notebooks that have a common origin or "ancestor". As no notebook in the test set has an ancestor in the training set, you may find this field to be of use as a grouping factor when constructing validation splits.
parent_id - Indicates that some version of the notebook id was forked from some version of the notebook parent_id. The notebook parent_id may or may not be present in the training data. (The parent may be missing because someone had forked a private notebook of their own, for instance.)
Example Test Data
To help you author submission code, we include a few example instances selected from the test set. When you submit your notebook for scoring, this example data will be replaced by the actual test data, including the sample_submission.csv file.

test/ - A few example notebooks from the test set. The actual test set comprises about 20,000 notebooks in a format similar to the training set notebooks. No notebook in the test set has an ancestor in the training set.
sample_submission.csv - A sample submission file in the correct format. See the Evaluation page for more details.

Competition Metric - Kendall Tau Correlation
Evaluation
We can compute the Kendall tau correlation between the predicted cell orders and the ground truth cell orders by counting how many swaps of adjacent cells are needed to sort the predicted order into the ground truth order.

A pair  i,j  of indices is called an inversion within a numeric sequence  A  when  i<j  but  A[i]>A[j] . An inversion indicates that a pair of numbers in the sequence is out of order. The number of swaps needed to correctly sort the predictions turns out to be equivalent to the number of inversions in its ranking of the cells relative to the ground-truth ranking.

The following cell shows an intuitive, but rather slow ( O(n2) ) way to count inversions in a list of ranks.

Predictions are evaluated by the Kendall tau correlation between predicted cell orders and ground truth cell orders accumulated across the entire collection of test set notebooks.

Let  be the number of swaps of adjacent entries needed to sort the predicted cell order into the ground truth cell order. In the worst case, a predicted order for a notebook with  cells will need  swaps to sort.

We sum the number of swaps from your predicted cell order across the entire collection of test set notebooks, and similarly with the worst-case number of swaps. We then compute the Kendall tau correlation as:


Contact 
--------
Kyndryl GCP Guild Moderator: Ramamurthy V 
GCP Contact: gcpguild@gmail.com
Date: June 21, 2022.
Revised : July 8, 2022
Contributors: 122 key members from Google Cloud Search API.

For SerpAPI Key request, please write an email request with an email subject of 'request for SerpApi Key'

"""
#-----------------------------------------------------#-----------------------------------------------------
githubserpaijson = "https://github.com/gcpguild/searpapi/blob/main/parseserpapijsongooglecloud.py"



import json, re, csv, os, unicodedata, requests, string, platform
import ijson
from bs4 import BeautifulSoup
from pathlib import Path
from six.moves.urllib.request import urlopen

import pandas as pd
from os import listdir

import urllib.request

import numpy as np

from requests import request
from urllib.error import URLError

from itertools import filterfalse
import json, re, csv, unicodedata, string, sys, glob
from pathlib import Path
import pandas as pd
from subprocess import check_output
#----------------------------------------------------------
def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        #C:\serpapi\python\app\nature-labs\google-cloud\data
               
        mymano = ''
        for x in clean_string:
            mymano += ''+ x
        return mymano
#---------------------------------------------------
def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#-----------------------------------------------------
def find_json_filenames( path_to_dir, suffix=".json" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]
# --------------------------------------------------------------------
def mkingdirs(givenlist):
    mymanog = N.join(givenlist)
    mk_dir = Path(mymanog)
    mk_dir.mkdir(parents=True, exist_ok=True)
    return mk_dir
#-------------------------------------------------------------------
def dataadding(inputfilename, head, l):
    tf = pd.DataFrame(l)
    modetw =  'a'
    tf.to_csv(inputfilename, encoding='utf-8', mode=modetw, index=False, header = False)
#---------------------------------------------------------------------------------
def gematerials(file_id, inputfilename, k, jd): 
    csvdatasheet = ("{}{}".format(inputfilename,'.csv'))
    mylist = [ getdirectory, 'output' , csvdatasheet ]
    templesserpapifilterdata = fullyqualifydirs(mylist)
    firstrow = ['id', 'cell_order']
    #cell_type
    if (k == 'cell_type'):
        results = jd[k]
        cleantemples = []
        g4c = []
        for impk, impv in results.items():
            #print(impk, impv)
            
            g4c.append(impk)
            nd = []
            #print(impk, impv)
             
        nd = [ file_id, ' '.join(str(x) for x in g4c)  ]
        print(nd)
        cleantemples.append(nd)
        dataadding( inputfilename = templesserpapifilterdata, head = firstrow, l = cleantemples)

#-------------------------------------------------------------------------------


def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")
#-------------------------------------------------------

myos = platform.system()

if (myos == "Linux" or myos == "linux2"):
    # linux
    N="/"
    homedirectory = str(Path.home())
    print(homedirectory)
    
    mylist = [ homedirectory, 'serpapi/python/app/nature-labs/GoogleAI4Code' ]
    basedir = fullyqualifydirs(mylist)
    print(basedir)
elif myos == "win32" or myos == "Windows":
    # Windows 
    N="\\"    
    basedir = 'C:\\serpapi\\python\\app\\nature-labs\\GoogleAI4Code'  
#--------------------------------------------------------------
if not basedir:
    basedir = os.getcwd()
#-----------------------------------------------------------------------------------------------------
mylist = [basedir, 'initialization.py']
initialdirectoryconfig = fullyqualifydirs(mylist)
#------------------------------------------------------------------------------------------------------
getdirectory = removen(check_output([sys.executable, initialdirectoryconfig], universal_newlines=True))
myoutdir = [getdirectory, 'output' ]
outputdir = mkingdirs(myoutdir)

mylist = [ getdirectory, 'test' ]

json_in_path_to_dir = find_json_filenames( path_to_dir = fullyqualifydirs(mylist))

serpapijsongooglecloud = json_in_path_to_dir 

for l in serpapijsongooglecloud:

    mylist = [ getdirectory,'test', l ]
    googlecloudservicejson = fullyqualifydirs(mylist)

    print(googlecloudservicejson)

    file_id = removen(re.sub(r'^.+/([^/]+)$', r'\1', os.path.splitext(googlecloudservicejson)[0]).split('\\')[-1])

    print(file_id)
    path = Path(googlecloudservicejson)

    if not path.is_file():
        pi="\'Kaggle JSON data is missing: \' :"
        p = ("{} {}".format(pi,googlecloudservicejson))
        prt(p)
        exit(1)
    #-----------------------------------------------------
    #-----------------------------------------------------


    inputfilename = 'sample_submission'   
    with open(googlecloudservicejson,"r", encoding="utf-8") as jf:
        data = json.load(jf)

    for key, value in data.items():
        templesgooglengine = []
        gematerials(file_id = file_id, inputfilename = inputfilename, k = key, jd = data)
#-----------------------------------------

