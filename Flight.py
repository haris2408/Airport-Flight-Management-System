from Airport import *


class Flight:
    def __init__(self, flightNo, origin, destination):
        # if not isinstance(origin, Airport) or not isinstance(destination, Airport):
        #     raise TypeError("the origin and destination must be airport objects")
        if not isinstance(origin, Airport):
            raise TypeError("the origin and destination must be airport objects")
        if not isinstance(destination, Airport):
            raise TypeError("the origin and destination must be airport objects")
        self._flightNo = flightNo
        self._origin = origin
        self._destination = destination

    def __repr__(self):
        if self.isDomesticFlight():
            return f"Flight: {self._flightNo} from {self._origin.getCity()} to {self._destination.getCity()} "+"{domestic}"
        else:
            return f"Flight: {self._flightNo} from {self._origin.getCity()} to {self._destination.getCity()} " + "{international}"

    def __eq__(self, other):
        if not isinstance(other, Flight):
            return False
        if self._origin.getCode() == other._origin.getCode() and self._destination.getCode() == other._destination.getCode():
            return True
        if self._origin.getCode() == other._destination.getCode() and self._destination.getCode() == other._origin.getCode():
            return True
        return False

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        return False

    def setOrigin(self, origin):
        if not isinstance(origin, Airport):
            raise TypeError("The origin must be Airport objects")
        self._origin = origin

    def setDestination(self, destination):
        if not isinstance(destination, Airport):
            raise TypeError("The destination must be Airport objects")
        self._origin = destination
