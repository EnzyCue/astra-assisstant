import spacy

nlp = spacy.load("en_core_web_sm")

class NounTracker:
    def __init__(self):
        self.noun_dict = {}
        self.noun_list = []

    def add_text(self, new_text):
        new_text = nlp(new_text)
        noun_chunker(new_text)


    #takes some tokenised text and chunks its nouns before appending them in oder into the noun_list
    def noun_chunker(self, text):
        for chunk in text.noun_chunks:

            self.noun_list.append(chunk)

            if self.noun_dict.has_key(chunk):
                self.noun_dict[chunk] += 1
            else:
                self.noun_dict = 1
