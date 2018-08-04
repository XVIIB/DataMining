import pandas as pd
inputfile = 'data/sales_data.xls'
data = pd.read_excel(inputfile, index_col=u'序号')

data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].as_matrix().astype(int)
y = data.iloc[:, 3].as_matrix().astype(int)

from sklearn.tree import DecisionTreeClassifier as DTC
dtc = DTC(criterion='entropy')
dtc.fit(x, y)

from sklearn.tree import export_graphviz
x = pd.DataFrame(x)
from sklearn.externals.six import StringIO
x = pd.DataFrame(x)
with open("tree1.doc", 'w') as f:
    f = export_graphviz(dtc, feature_names=x.columns, out_file=  f)


