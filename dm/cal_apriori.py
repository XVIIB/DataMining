from __future__ import  print_function
import  pandas as pd
from apriory import *

inputfile = 'data/menu_orders.xls'
outputfile = 'temp/apriori_rules.xls'
data = pd.read_excel(inputfile, header= None)

print(u'\n数据转入矩阵')
ct = lambda  x : pd.Series(1, index= x[pd.notnull(x)])
b = map(ct, data.as_matrix())
data = pd.DataFrame(list(b)).fillna(0)
print(u'\n转换完毕')
del b

support = 0.2
confidence = 0.5
ms = '-----'

find_rule(data,support, confidence, ms).to_excel(outputfile)