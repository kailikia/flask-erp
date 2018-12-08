# class - collection of related methids and variables
# methods - function inside a class
# obeject - instance of a class
# constructor - first method that runs when class is instantiated

class PayrollCalculator:
    payee=0
    nssf = 0
    nhif = 0
    grossSalary = 0


    def __init__(self,basicsalary,overtime,houseallowance,otherbenefits):
        self.grossSalary = int(basicsalary) + int(overtime) + int(otherbenefits) + int(houseallowance)
        self.getPAYEE()
        self.getNHIF()
        self.getNSSF()

    def getPAYEE(self):
        gross = self.grossSalary
        if gross >= 47059:
            numpayee = int(gross) * 0.3
        elif gross > 35473 and gross <= 47059:
            numpayee = int(gross) * 0.25
        elif gross > 23886 and gross <= 35472:
            numpayee = int(gross) * 0.2
        elif gross > 12299 and gross <= 23885:
            numapayee = int(gross) * 0.15
        elif gross <= 12298:
            numpayee = int(gross) * 0.1
        self.payee = int(numpayee)

    def getNHIF(self):
        gross = self.grossSalary
        if gross >= 100000:
            nhif = 1700
        elif gross > 90000 and gross <= 99999:
            nhif = 1600
        elif gross > 80000 and gross <= 89999:
            nhif = 1500
        elif gross > 70000 and gross <= 79999:
            nhif = 750
        elif gross > 60000 and gross <= 69999:
            nhif = 600
        elif gross > 50000 and gross <= 59999:
            nhif = 500
        elif gross > 45000 and gross <= 49999:
            nhif = 400
        elif gross > 40000 and gross <= 44999:
            nhif = 300
        elif gross > 35000 and gross <= 39999:
            nhif = 950
        elif gross > 30000 and gross <= 34999:
            nhif = 900
        elif gross > 25000 and gross <= 29999:
            nhif = 850
        elif gross > 20000 and gross <= 24999:
            nhif = 750
        elif gross > 15000 and gross <= 19999:
            nhif = 600
        elif gross > 12000 and gross <= 14999:
            nhif = 500
        elif gross > 8000 and gross <= 11999:
            nhif = 400
        elif gross > 6000 and gross <= 7999:
            nhif = 300
        elif gross <= 5999:
            nhif = 150
        self.nhif = int(nhif)

    def getNSSF(self):
        gross = self.grossSalary
        if gross >= 18000:
            numnssf = 1080
        elif gross >= 6001 and gross <= 18000:
            numnssf = gross * 0.06
        elif gross <= 6000:
                numnssf = 360
        self.nssf = int(numnssf)



