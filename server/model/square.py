import json

class Square:

    id = 0
    image = 'square'
    open = False


    def __init__(self, id=None):
        self.id = id
        self.image = 'square'
        self.open = False

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
