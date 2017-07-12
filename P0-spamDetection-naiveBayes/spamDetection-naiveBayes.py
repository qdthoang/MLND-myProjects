"""
Dataset from - https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
"""

import pandas


# import data set, name the columns
data = pandas.read_table('smsspamcollection/SMSSpamCollection',
                         sep='\t', # tab separated
                         header=None,
                         names=['label', 'sms_message'])
print(data.head()) # print first 5 rows


# mapping label values
data['label'] = data.label.map({'ham':0, 'spam':1})
print(data.shape) # print number of rows and columns (respectively)


# data processing with CountVectorizer()
from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()
count_vector.fit(data)
print(count_vector.get_feature_names())


# split data into training and testing sets
# X_train = training data for 'sms_message' column
# X_test = testing data for 'sms_message' column
# y_train = training data for 'label' column
# y_test = testing data for 'label' column
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data['sms_message'],
                                                    data['label'],
                                                    random_state=1)

print('Number of rows in the total set: {}'.format(data.shape[0]))
print('Number of rows in the training set: {}'.format(X_train.shape[0]))
print('Number of rows in the test set: {}'.format(X_test.shape[0]))


''' applying Bag of Words '''
# import and init
from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()

# fit training data and return matrix
training_data = count_vector.fit_transform(X_train)

# transform testing data and return matrix
testing_data = count_vector.transform(X_test)


''' applying Naive Bayes  '''
# import and init
from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()

# fit the training data into the MultinomialNB()
naive_bayes.fit(training_data, y_train)

# make predictions on the test data
predictions = naive_bayes.predict(testing_data)


''' 
Accuracy = [correct prediction / total predictions] 
    '-> how often the classifier makes the correct prediction
Precision = [True Positives / (True Positives + False Positives)]
    '-> what proportion of messages we classified as spam, actually were spam
Recall(sensitivity) = [True Positives/(True Positives + False Negatives)]
    '-> what proportion of messages that actually were spam were classified by us as spam
'''
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print 'Accuracy score:',\
    format(accuracy_score(y_test, predictions))
print 'Precision score:',\
    format(precision_score(y_test, predictions))
print 'Recall score:',\
    format(recall_score(y_test, predictions))
print 'F1 score:',\
    format(f1_score(y_test, predictions))