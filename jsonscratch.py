import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# decode to object
class Todo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

def encode_todo(todo):
    if isinstance(todo, Todo):
        return {"__Todo__":True,"userId":todo.userId,
                "id":todo.id, "title":todo.title, "completed":todo.completed}
    else:
        type_name = todo.__class__.__name__
        raise TypeError("Object of type %s is not JSON serializable" %
                        type_name)


def decode_todo(dct):
    if '__Todo__' in dct:
        return Todo(dct['userId'],dct['id'],dct['title'],dct['completed'])
    return dct
