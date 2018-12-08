from peewee import *
try:
    db = PostgresqlDatabase('d5b2qm4dpmt453', user='qwcrlfygilfxwz', password="14dcc470668a7efbc8e0f055482d862f145d9e372c81f9bec77b6dd0b9701917", host="ec2-54-235-156-60.compute-1.amazonaws.com")
    print("Successfully connected!")
except:
    print("Didn't connect!")


class Employee(Model):
    full_name = CharField()
    kra_pin_number = CharField()
    department = CharField()
    position = CharField()
    basic_salary = FloatField()
    house_allowance = FloatField()

    class Meta:
        database = db # This model uses the "people.db" database.
        table_name = "employees"


Employee.create_table(fail_silently=True)