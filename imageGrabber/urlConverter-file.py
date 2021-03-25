import sys
import pandas as pd
import requests
import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('links', metavar='N', type=str, nargs='+', help='Url links to convert')
parser.add_argument("-fn", "--filename", help="File Name", dest='filename', default="./convertedImages")
args = parser.parse_args()

links = [i for i in pd.read_csv(x) for x in args.links]

try:
    os.mkdir(args.filename)
except FileExistsError:
    pass

for i, x in enumerate(links):
    req = requests.get(x)
    fileName = (re.search(r'/[^/]*\.[psj][pvn].*g?', x)).group()[1:]
    print("saving " + fileName)
    with open(f'{args.filename}/{fileName}', 'wb') as file:
        file.write(req.content)

