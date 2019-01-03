import json

"""

"""
class Monad:
    def __init__(self, title, text=""):
        self.text = text
        self.title = title

    def print_monad(self):
        print((self.title,self.text))

def encode_monad(monad):
    if isinstance(monad, Monad):
        return {"__Monad__":True , "title" : monad.title,"text":monad.text}
    else:
        type_name = monad.__class__.__name__
        raise TypeError("Object of type %s is not JSON serializable" %
                        type_name) 

def decode_monad(dict):
    if "__Monad__" in dict:
        return Monad(title = dict['title'], text = dict['text'])
    return dict
