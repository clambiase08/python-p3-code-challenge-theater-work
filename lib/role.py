from lib.audition import Audition


class Role:
    all = []

    def __init__(self, character_name):
        self.character_name = character_name
        Role.all.append(self)

    @property
    def character_name(self):
        return self._character_name

    @character_name.setter
    def character_name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._character_name = value
        else:
            raise Exception

    def auditions(self):
        return [audition for audition in Audition.all if audition.role == self]

    def actors(self):
        return list(
            [audition.actor for audition in Audition.all if audition.role == self]
        )

    def locations(self):
        return list(
            [audition.location for audition in Audition.all if audition.role == self]
        )

    def lead(self):
        hired_auditions = [audition for audition in self.auditions() if audition.hired]
        if not hired_auditions:
            return "no actor has been hired for this role"
        else:
            return hired_auditions[0]

    def understudy(self):
        understudy_auditions = [
            audition for audition in self.auditions() if audition.hired
        ]
        if len(understudy_auditions) <= 1:
            return "no actor has been hired for understudy for this role"
        else:
            return understudy_auditions[1]

    @classmethod
    def not_cast(cls):
        return [
            role
            for role in cls.all
            if not any([audition.hired for audition in role.auditions()])
        ]
