class Airport:
    def __init__(self,code,city,country):
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):
        return f"{self._code} ({self._city}, {self._country})"

    def __eq__(self, other):
        if not isinstance(other,Airport):
            raise TypeError("Not an airport instance")
        if (self._code == other._code) and (self._city == other._city) and (self._country == other._country):
            return True
        return False

    def getCode(self):
        return self._code

    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country

    def setCity(self, city):
        self._city = city

    def setCountry(self, country):
        self._country = country
