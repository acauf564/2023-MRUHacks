class Assignment:

    def __init__(self, desc, date, weight) -> None:
        self.description = desc
        self.date = date
        self.weight = float(self.cleanWeight(weight))
        self.priority = self.setPriority()
        self.assigned_hours = self.calculateHours()

    def calculateHours(self) -> float:
        if self.priority == 10:
            return 2
        elif self.priority == 9:
            return 6
        elif self.priority == 8:
            return 10
        elif self.priority == 7:
            return 14
        elif self.priority == 6:
            return 18
        elif self.priority == 5:
            return 22
        elif self.priority == 4:
            return 26
        elif self.priority == 3:
            return 30
        elif self.priority == 2:
            return 34
        else:
            return 38

    def cleanWeight(self, rawString):
        if '%' in rawString:
            rawString = rawString.replace('%', '')
        return rawString

    def setPriority(self) -> int:
        if self.weight < 10:
            return 10
        elif self.weight < 20:
            return 9
        elif self.weight < 30:
            return 8
        elif self.weight < 40:
            return 7
        elif self.weight < 50:
            return 6
        elif self.weight < 60:
            return 5
        elif self.weight < 70:
            return 4
        elif self.weight < 80:
            return 3
        elif self.weight < 90:
            return 2
        else:
            return 1

    def getDescription(self) -> str:
        return self.description

    def setDescription(self, newDesc) -> None:
        self.description = newDesc

    def getDate(self) -> str:
        return self.date

    def setDescription(self, newDate) -> None:
        self.date = newDate

    def getWeight(self) -> str:
        return self.weight

    def setDescription(self, newWeight) -> None:
        self.weight = newWeight
