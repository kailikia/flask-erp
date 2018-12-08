def getNetSalary(gross,deduction):
    net_salary=int(gross)-int(deduction)
    return net_salary

def getGrossSalary(basic,benefits):
    gross_salary=int(basic)+int(benefits)
    return gross_salary

def getBenefits(overtime,house,other):
    benefits=int(overtime)+int(house)+int(other)
    return benefits

def getDeductions(payee,NHIF,NSSF):
    deduction=int(payee)+int(NHIF)+int(NSSF)
    return deduction

def getPayee(gross):
    LIMIT_1 = 12298
    LIMIT_2 = 23885
    LIMIT_3 = 35472
    LIMIT_4 = 47059
    LIMIT_5 = 47060

    RATE_1 = 0.10
    RATE_2 = 0.15
    RATE_3 = 0.20
    RATE_4 = 0.25
    RATE_5 = 0.30
    if gross <= LIMIT_1:
        payee = RATE_1 * gross
    elif gross < LIMIT_2:
        payee = RATE_1 * LIMIT_1 + RATE_2 * (gross - LIMIT_1)
    elif gross <= LIMIT_3:
        payee = RATE_1 * LIMIT_1 + RATE_2 * (LIMIT_2  - LIMIT_1) + \
              RATE_3 * (gross -  LIMIT_2)
    elif gross <= LIMIT_4:
        payee = RATE_1 * LIMIT_1 + RATE_2 * (LIMIT_2 - LIMIT_1) + \
              RATE_3 * (LIMIT_3 - LIMIT_2) + RATE_4 * (gross - LIMIT_3)
    elif gross < LIMIT_5:
        payee = RATE_1 * LIMIT_1 + RATE_2 * (LIMIT_2 - LIMIT_1) + \
        RATE_3 * (LIMIT_3 - LIMIT_2) + RATE_4 * (LIMIT_4 - LIMIT_3) + \
              RATE_5 * (gross - LIMIT_4)
    return payee

def getNHIF(gross):
    if gross <=5999:
        NHIF=150
    elif gross >=6000 and gross<=7999:
        NHIF=300
    elif gross>=8000 and gross<=11999:
        NHIF=400
    elif gross>=12000 and gross<=14999:
        NHIF=500
    elif gross>=15000 and gross<=19999:
        NHIF=600
    elif gross>=20000 and gross<=24999:
        NHIF=750
    elif gross>=25000 and gross<=29999:
        NHIF=850
    elif gross>=30000 and gross<=34999:
        NHIF=900
    elif gross>=35000 and gross<=39999:
        NHIF=950
    elif gross>=40000 and gross<=44999:
        NHIF=1000
    elif gross>=45000 and gross<=49999:
        NHIF=1100
    elif gross>=50000 and gross<=59999:
        NHIF=1200
    elif gross>=60000 and gross<=69999:
        NHIF=1300
    elif gross>=70000 and gross<=79999:
        NHIF=1400
    elif gross>=80000 and gross<=89999:
        NHIF=1500
    elif gross>=90000 and gross<=99999:
        NHIF=1600
    elif gross>=100000:
        NHIF=1700
    return NHIF

def getNSSF(gross):
    if gross<=6000:
        NSSF=360
    elif gross>=6001 and gross<=18000:
        NSSF=int(gross)*0.06
    elif gross>18000:
        NSSF=1080
    return NSSF

basic=input("Please input monthly basic salary:")
overtime=input("Please input monthly overtime salary:")
house=input("Please input monthly house benefit:")
other=input("Please input monthly other benefits:")

benefitCal=getBenefits(overtime,house,other)
grossCal=getGrossSalary(basic,benefitCal)
payeeCal=getPayee(grossCal)
NHIFCal=getNHIF(grossCal)
NSSFCal=getNSSF(grossCal)
deductionCal=getDeductions(payeeCal,NHIFCal,NSSFCal)
netCal=getNetSalary(grossCal,deductionCal)


print("Benefit is:",benefitCal)
print("Gross salary is:",grossCal)
print("Net salary is:",netCal)
