import ipdb

from lib.audition import Audition
from lib.role import Role

macbeth = Role("Macbeth")
juliet = Role("Juliet")

audition = Audition(macbeth, "leonardo", "nyc", "2121231234")
# audition_two = Audition(juliet, 20, "la", "9991231234")


ipdb.set_trace()
