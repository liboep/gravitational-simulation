class Galaxy:
    def __init__(self, name):
        self.name = name
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def get_all_bodies(self):
        return self.bodies
