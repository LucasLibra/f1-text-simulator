class Driver:
        def __init__(self, name, number, nationality, team, tyre_compound, tyre_age):
                self.name = name
                self.team = team
                self.number = number
                self.nationality = nationality
                self.tyre_compound = tyre_compound
                self.tyre_age = tyre_age
                self.race_time = 0
        
        def getName(self):
            return self.name

        def getNationality(self):
            return self.nationality

        def getTyreAge(self):
            return self.tyre_age

        def getTyreCompound(self):
            return self.tyre_compound
        
        def getTeam(self):
            return self.team
        
        def getNumber(self):
            return self.number

        def getRaceTime(self):
            return self.race_time

        def setTyreAge(self, tyre_age):
            self.tyre_age = tyre_age

        def setRaceTime(self, race_time):
            self.race_time = race_time

        def setTyreCompound(self, tyre_compound):
            self.tyre_compound = tyre_compound