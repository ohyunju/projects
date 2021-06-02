import os
import csv

yes24_FILEPATH = os.path.join(os.getcwd(), 'project_app', 'yes24.csv')
kyobo_FILEPATH = os.path.join(os.getcwd(), 'project_app', 'kyobo.csv')
aladdin_FILEPATH = os.path.join(os.getcwd(), 'project_app', 'aladdin.csv')

raw_sell=[]
with open(yes24_FILEPATH, 'r', encoding='utf-8') as yes24:
    yes24_reader = csv.DictReader(yes24)

    raw_sell=[]
    for cols in yes24_reader:
        #print(cols)
        raw_sell.append(cols)
    
    print(raw_sell)
        
    title = raw_sell[0]['title']
    print(title)    
    # col_names = next(yes24_reader)
    # print(col_names)

#   for cols in yes24_reader:
#     doc = {col_name: col for col_name, col in zip(col_names, cols)}
#     raw_sell.append(doc)
# add_bestsells(raw_sell,which='yes24')

