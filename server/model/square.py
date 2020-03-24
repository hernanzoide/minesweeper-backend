import json

class Square:

    def __init__(self, id, image):
        self.id = id
        self.image = image
        self.open = False

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
