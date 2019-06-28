# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import re

path = 'MYH7_Luis_Lopes.xlsx'
 
accession_code = "P12883"


df = pd.read_excel (r'MYH7_Luis_Lopes.xlsx') 
#print (df)



df = pd.ExcelFile('MYH7_Luis_Lopes.xlsx').parse('Majid MYH7') 
x=[]
x.append(df['MYH7protein'])

native_residue=list()
residue_number=list()
mutant_residue =list()
pattern=re.compile("(\w)(\d+)(\w)")



for i, line in enumerate(df['MYH7protein']):
    if not pd.isnull(line):
        matches = re.findall(pattern, line)
        if len(matches) == 1:
            match = matches[0]
            if (len(match)) == 3:
                native_residue.append(match[0])
                residue_number.append(match[1])
                mutant_residue.append(match[2])
                print(accession_code, native_residue[-1], residue_number[-1], mutant_residue[-1])

#print("Found %d", len(native_residue))





