from Flight import *
from Airport import *

allAirports = list()
allFlights = dict()


def loadData(airportFile, flightFile):
    try:
        with open(airportFile, 'r') as af:
            lines = af.readlines()
            for line in lines:
                splitLines = line.split(",")
                code = splitLines[0].strip()
                country = splitLines[1].strip()
                city = splitLines[2].strip()
                city = city.replace('\n', '')
                newAirport = Airport(code, city, country)
                allAirports.append(newAirport)
    except:
        return False
    try:
        with open(flightFile, 'r') as ff:
            lines = ff.readlines()
            for line in lines:
                splitLines = line.split(",")
                flightCode = splitLines[0].strip()
                originCode = splitLines[1].strip()
                origin = getAirportByCode(originCode)
                destCode = splitLines[2].strip()
                destCode = destCode.replace('\n', '')
                dest = getAirportByCode(destCode)
                newFlight = Flight(flightCode, origin, dest)
                if originCode not in allFlights.keys():
                    allFlights[originCode] = [newFlight]
                else:
                    allFlights[originCode].append(newFlight)
    except:
        return False
    return True


def getAirportByCode(code):
    for airport in allAirports:
        if airport.getCode() == code:
            return airport


def findAllCityFlights(city):
    ans = []
    for key in allFlights.keys():
        for flight in allFlights[key]:
            if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city:
                ans.append(flight)
    return ans


def findAllCountryFlights(Country):
    ans = []
    for key in allFlights.keys():
        for flight in allFlights[key]:
            if flight.getOrigin().getCountry() == Country or flight.getDestination().getCountry() == Country:
                ans.append(flight)
    return ans


def findFlightBetween(origAirport, destAirport):
    X = set()
    for a in allFlights[origAirport.getCode()]:
        if a.getOrigin() == origAirport:
            if a.getDestination() == destAirport:
                return f"Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}"
            else:
                for b in allFlights[a.getDestination().getCode()]:
                    if b.getOrigin() == a.getDestination() and b.getDestination() == destAirport:
                        X.add(a.getDestination().getCode())
    if X:
        return X
    return -1


# def findFlightBetween(origAirport, destAirport):
#     for key in allFlights.keys():
#         for flight in allFlights[key]:
#             if flight.getOrigin() == origAirport:
#                 if flight.getDestination() == destAirport:
#                     return f"Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}"
#                 else:
#                     fromOrigin = findAllCityFlights(flight.getOrigin().getCity())
#                     fromOrigin_actual = []
#                     for a in fromOrigin:
#                         if a.getOrigin() == origAirport:
#                             fromOrigin_actual.append(a)
#                     X = set()
#                     for a in fromOrigin_actual:
#                         toDest = findAllCityFlights(a.getDestination().getCity())
#                         for b in toDest:
#                             if b.getOrigin() == a.getOrigin() and b.getDestination() == destAirport:
#                                 X.add(b.getOrigin().getCode())
#                     if X:
#                         return X
#     return -1

def findReturnFlight(firstFlight):
    for a in allFlights[firstFlight.getDestination().getCode()]:
        if a == firstFlight:
            return a
    return -1

# loadData("airports.txt", "flights.txt")
# a = findAllCityFlights("Shanghai")
# print(a)
# b = findAllCountryFlights("China")
# print(b)
#
# f1 = findFlightBetween(getAirportByCode("PVG"), getAirportByCode("YOW"))
# print(f1)
