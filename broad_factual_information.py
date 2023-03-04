import spacy

nlp = spacy.load("en_core_web_sm")

class TypeOne:
    def __init__(self, text):
        self.text = nlp(text)
        self.proper_noun = None
        self.noun = None


    def length_check(self):
        return len(self.text)

    def has_proper_noun(self):
        for token in self.text:
            if token.pos_ == "PROPN":
                self.set_proper_noun(token)
                return True
        return False


    def set_proper_noun(self, proper_noun):
        self.proper_noun = proper_noun

    def get_proper_noun(self):
        for token in self.text:
            if token.pos_ == "PROPN":
                self.set_proper_noun(token)
                return token
        return False

    def has_noun(self):
        for token in self.text:
            if token.pos_ == "NOUN":
                self.set_noun(token)
                return True
        return False

    def set_noun(self, noun):
        self.noun = noun

    def get_noun(self):
        for token in self.text:
            if token.pos_ == "NOUN":
                self.set_noun(token)
                return token
        return False