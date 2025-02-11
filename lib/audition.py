class Audition:
    all = []

    def __init__(self, role, actor, location, phone):
        self.role = role
        self.actor = actor
        self.location = location
        self.phone = phone
        self.hired = False
        Audition.all.append(self)

    @property
    def actor(self):
        return self._actor

    @actor.setter
    def actor(self, value):
        if type(value) == str and 20 > len(value) > 3:
            self._actor = value
        else:
            raise Exception

    def call_back(self):
        self.hired = True
