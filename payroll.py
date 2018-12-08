from employee import *

class Payroll(Model):
    payroll_date = DateField()
    overtime = FloatField()
    other_benefits = FloatField()
    nhif = FloatField()
    nssf = FloatField()
    payee = FloatField()
    employee_id = ForeignKeyField(Employee,to_field="id",on_update="cascade")


    class Meta:
        database = db # This model uses the "people.db" database.
        table_name = "payrollss"

Payroll.create_table(fail_silently=True)