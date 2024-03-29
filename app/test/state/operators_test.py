import uuid
from datetime import datetime
from app.models.event import Event
from app.models.pilot import Pilot
from app.models.event_gene import EventGene
from app.constants.quals import TRANS

"""
operators test state
"""

# event ids
uuid1 = uuid.UUID('00000000-0000-0000-0000-000000000001')
uuid2 = uuid.UUID('00000000-0000-0000-0000-000000000002')
uuid3 = uuid.UUID('00000000-0000-0000-0000-000000000003')

# events
event30 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 8, 0), "flight", TRANS)
event30.id = uuid1
event31 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 8, 0), "flight", TRANS)
event31.id = uuid2
event32 = Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 10, 0), "flight", TRANS)
event32.id = uuid3

op_events = {
    event30.id: event30,
    event31.id: event31,
    event32.id: event32,
}

# pilots
pilot30 = Pilot("Steamboat", [TRANS])
pilot31 = Pilot("Dump", [TRANS])
pilot32 = Pilot("Tummy", [TRANS])
pilot33 = Pilot("Virgil", [TRANS])
pilot34 = Pilot("Topper", [TRANS])
pilot35 = Pilot("Spacecamp", [TRANS])
pilot36 = Pilot("Jambles", [TRANS])
pilot37 = Pilot("Beef", [TRANS])
pilot38 = Pilot("Donk", [TRANS])

op_pilots = {
    pilot30.id: pilot30,
    pilot31.id: pilot31,
    pilot32.id: pilot32,
    pilot33.id: pilot33,
    pilot34.id: pilot34,
    pilot35.id: pilot35,
    pilot36.id: pilot36,
    pilot37.id: pilot37,
    pilot38.id: pilot38,
}

schedule = [EventGene(uuid1), EventGene(uuid2), EventGene(uuid3)]

sched_alleles = {
    uuid1: [pilot30.id, pilot31.id, pilot32.id],
    uuid2: [pilot33.id, pilot34.id, pilot35.id],
    uuid3: [pilot36.id, pilot37.id, pilot38.id],
}
