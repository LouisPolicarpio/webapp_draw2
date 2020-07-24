import csv
import os
from app_webapp_draw.models import Verb

def run():

    workpath = os.path.dirname(os.path.abspath(__file__))
    fhand = open(os.path.join(workpath,'word_lists/english-word-list-verbs.csv'))
    reader = csv.reader(fhand, delimiter = ";")

    next(reader)
    next(reader)
    next(reader)
    next(reader)

    for row in reader:
        #print(row[1])
        adj = Verb(word = row[1])
        adj.save()
