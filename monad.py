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

def create_monad_CLI():
    print('This will create a monad from the command line. You can either',
          'type the text yourself of point to a file which has the text in it')
    print('First input the title of the monad you want to create')
    title = input()

    print('next specify the file name where the text is')
    filename = input()

    with open(filename, 'r') as file:
        text = file.read()

    m1 = Monad(title, text)
    commit_monad(m1)

def get_monad_list():
    with open('monad_master.json','r') as file:
        mon_list = json.load(file, object_hook=decode_monad)
    return mon_list

def save_monad_master(mon_list):
    with open('monad_master.json','w') as file:
        json.dump(mon_list, file, default=encode_monad)

def print_monad_list():
    mon_list = get_monad_list()
    for mon in mon_list:
        print(mon.title)
    
def commit_monad(monad):
    monlist = get_monad_list()
    monlist.append(monad)
    save_monad_master(monlist)
