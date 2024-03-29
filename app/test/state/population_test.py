from datetime import datetime
from app.models.event import Event
from app.models.pilot import Pilot
from app.models.event_gene import EventGene
from app.constants.quals import TRANS

"""
Population Test State (2x)
"""

event20 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 8, 0), "flight", TRANS)
event21 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 8, 0), "flight", TRANS)
event22 = Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 10, 0), "flight", TRANS)
event23 = Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 10, 0), "flight", TRANS)
event24 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 0), "flight", TRANS)
event25 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 0), "flight", TRANS)
event26 = Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 0), "flight", TRANS)
event27 = Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 0), "flight", TRANS)
event28 = Event(datetime(2019, 1, 1, 22, 0), datetime(2019, 1, 1, 23, 0), "flight", TRANS)
event29 = Event(datetime(2019, 1, 1, 22, 0), datetime(2019, 1, 1, 23, 0), "flight", TRANS)

pilot20 = Pilot("Steamboat", [TRANS])
pilot21 = Pilot("Dump", [TRANS])
pilot22 = Pilot("Tummy", [TRANS])
pilot23 = Pilot("Virgil", [TRANS])
pilot24 = Pilot("Topper", [TRANS])
pilot25 = Pilot("Spacecamp", [TRANS])
pilot26 = Pilot("Jambles", [TRANS])
pilot27 = Pilot("Beef", [TRANS])

pop_pilots = {
    pilot20.id: pilot20,
    pilot21.id: pilot21,
    pilot22.id: pilot22,
    pilot23.id: pilot23,
    pilot24.id: pilot24,
    pilot25.id: pilot25,
    pilot26.id: pilot26,
    pilot27.id: pilot27,
}

pop_events = {
    event20.id: event20,
    event21.id: event21,
    event22.id: event22,
    event23.id: event23,
    event24.id: event24,
    event25.id: event25,
    event26.id: event26,
    event27.id: event27,
    event28.id: event28,
    event29.id: event29,
}

pop_sched = [
    EventGene(event20.id),
    EventGene(event21.id),
    EventGene(event22.id),
    EventGene(event23.id),
    EventGene(event24.id),
    EventGene(event25.id),
    EventGene(event26.id),
    EventGene(event27.id),
    EventGene(event28.id),
    EventGene(event29.id),
]

pop_sched_alleles = {
    event20.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event21.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event22.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event23.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event24.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event25.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event26.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event27.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event28.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event29.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
}
