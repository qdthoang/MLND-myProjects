documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

# convert all entries to lower case
lower_case_documents = []
for i in documents:
    lower_case_documents.append(i.lower())
print(lower_case_documents)

# remove all punctuation
import string
sans_punctuation_documents = []
for i in lower_case_documents:
    sans_punctuation_documents.append(i.translate(None, string.punctuation))
print(sans_punctuation_documents)

# tokenization
preprocessed_documents = []
for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split())
print(preprocessed_documents)

# count frequencies
frequency_list = []
import pprint
from collections import Counter
for i in preprocessed_documents:
    frequency_counts = Counter(i)
    frequency_list.append(frequency_counts)
print(frequency_list)
pprint.pprint(frequency_list)