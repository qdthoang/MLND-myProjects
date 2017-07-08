'''
Dataset from - https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
'''

import pandas

# import data set, name the columns
data = pandas.read_table('smsspamcollection/SMSSpamCollection',
                         sep='\t', # tab separated
                         header=None,
                         names=['label', 'sms_message'])

# mapping label values
data['label'] = data.label.map({'ham':0, 'spam':1})

print(data.head()) # print first 5 rows
print(data.shape) # print number of rows and columns (respectively)
