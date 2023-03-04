from spacy.tokens import DocBin
import spacy
import os
import csv
nlp = spacy.load("en_core_web_sm")
dirname = os.path.dirname(__file__)

#check README before implementing

# I know this code is kind ugly but this is just used to take my csv Spacy_Neural_Network_Data and convert into spacy Spacy_Neural_Network_Data for the
# spacy neural network to use when generating my model. I also think it looks more clear this way.

# While in the process of converting my Spacy_Neural_Network_Data I also assign values for spacy to use when applying its
# gradient descent algorithms. Those are my 1s and 0s in make_docs



#take in Spacy_Neural_Network_Data from my CSVs

with open(os.path.join(dirname, 'CSV_Inputs\Train.csv')) as f:
    train_data = [tuple(line) for line in csv.reader(f)]

with open(os.path.join(dirname, 'CSV_Inputs\Validate.csv')) as f:
    valid_data = [tuple(line) for line in csv.reader(f)]


#pipe my Spacy_Neural_Network_Data into spacy while also inputting their values
def make_docs(data):
    docs = []
    for doc, label in nlp.pipe(data, as_tuples=True):
        if label == "I":
            doc.cats["Type I"] = 1
            doc.cats["Type II"] = 0
            doc.cats["Type III"] = 0
            doc.cats["Type IV"] = 0

        elif label == "II":
            doc.cats["Type I"] = 0
            doc.cats["Type II"] = 1
            doc.cats["Type III"] = 0
            doc.cats["Type IV"] = 0

        elif label == "III":
            doc.cats["Type I"] = 0
            doc.cats["Type II"] = 0
            doc.cats["Type III"] = 1
            doc.cats["Type IV"] = 0


        elif label == "IV":
            doc.cats["Type I"] = 0
            doc.cats["Type II"] = 0
            doc.cats["Type III"] = 0
            doc.cats["Type IV"] = 1
        docs.append(doc)
    return (docs)

#create the spacy Spacy_Neural_Network_Data documents for the neural network to use
train_docs = make_docs(train_data[:302])
doc_bin = DocBin(docs=train_docs)
doc_bin.to_disk(os.path.join(dirname, 'Spacy_Neural_Network_Data/train.spacy'))

valid_docs = make_docs(valid_data[:27])
doc_bin = DocBin(docs=valid_docs)
doc_bin.to_disk(os.path.join(dirname, 'Spacy_Neural_Network_Data/validate.spacy'))

