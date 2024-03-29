"""
The Pilot Model
"""

import uuid
from typing import List

class Pilot():
    """
    Represents a single pilot and the data associated.
    """

    def __init__(self, callsign: str = '', quals: List[str] = None,
                 snivs: List[uuid.UUID] = None, plt: bool = True,
                 last_odo: int = 0) -> None:
        """
        Creates a Pilot

        Args:
            callsign: pilot's callsign
            quals: list of pilot's quals using standard sting constants
            snivs: list of pilot's snivs
            plt: True if this is a pilot, False if a WSO
            last_odo: days since last ODO this pilot stood

        Returns:
            None
        """

        self.id = uuid.uuid4()
        self.callsign = callsign
        self.quals = quals if quals else []
        self.snivs = snivs if snivs else []
        self.last_odo = last_odo
        self.last_odo_norm = 0
        self.plt = plt

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, the_id: uuid.UUID):
        self._id = the_id

    @property
    def callsign(self) -> str:
        return self._callsign

    @callsign.setter
    def callsign(self, callsign: str) -> None:
        self._callsign = callsign

    @property
    def quals(self) -> List[str]:
        return self._quals

    @quals.setter
    def quals(self, quals: List[str]) -> None:
        self._quals = quals

    @property
    def snivs(self) -> List[uuid.UUID]:
        return self._snivs

    @snivs.setter
    def snivs(self, snivs: List[uuid.UUID]) -> None:
        self._snivs = snivs

    @property
    def plt(self) -> bool:
        return self._plt

    @plt.setter
    def plt(self, plt: bool) -> None:
        self._plt = plt

    @property
    def last_odo(self) -> int:
        return self._last_odo

    @last_odo.setter
    def last_odo(self, last_odo: int) -> None:
        self._last_odo = last_odo

    @property
    def last_odo_norm(self) -> float:
        return self._last_odo_norm

    @last_odo_norm.setter
    def last_odo_norm(self, norm: float) -> None:
        self._last_odo_norm = norm

    def __repr__(self) -> str:
        return "pilotId {}".format(self.id.urn)
