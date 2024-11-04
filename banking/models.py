from django.db import models
from decimal import Decimal

class Bank(models.Model):
    B_ID = models.AutoField(primary_key=True)
    B_Name = models.CharField(max_length=50)
    Grade = models.CharField(max_length=1)
    B_Address = models.CharField(max_length=50, blank=True, null=True)
    Website = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Bank'

class Branch(models.Model):
    Branch_id = models.IntegerField(primary_key=True)
    Br_Name = models.CharField(max_length=50)
    Bank_ID = models.ForeignKey('Bank', on_delete=models.CASCADE, db_column='Bank_ID', related_name='branches')
    Br_Address = models.CharField(max_length=100, blank=True, null=True)
    Br_Phone = models.CharField(max_length=10)

    class Meta:
        db_table = 'Branch'

class Employee(models.Model):
    E_id = models.AutoField(primary_key=True)
    Branch_id = models.ForeignKey('Branch', on_delete=models.CASCADE, db_column='Branch_id', related_name='employees')
    E_Name = models.CharField(max_length=50)
    Position = models.CharField(max_length=50, blank=True, null=True)
    Salary = models.CharField(max_length=7)
    Gender = models.CharField(max_length=1, blank=True, null=True)
    E_phone = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'Employee'

class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    C_id = models.AutoField(primary_key=True)
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE, db_column='Branch_id', related_name='customers')
    C_Name = models.CharField(max_length=50)
    C_Address = models.CharField(max_length=255, blank=True, null=True)
    DOB = models.DateField()
    C_phone = models.CharField(max_length=10)
    Nationality = models.CharField(max_length=50, blank=True, null=True)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'Customer'

class Account(models.Model):
    ACCOUNT_STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('CLOSED', 'Closed'),
    ]

    Acc_id = models.BigIntegerField(primary_key=True)
    C_id = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='C_id', related_name='accounts')
    Acc_type = models.CharField(max_length=20)
    Balance = models.DecimalField(max_digits=15, decimal_places=2)
    Acc_status = models.CharField(max_length=10, choices=ACCOUNT_STATUS_CHOICES, default='ACTIVE')
    Opened_date = models.DateField()

    class Meta:
        db_table = 'Account'

class Loan(models.Model):
    L_id = models.AutoField(primary_key=True)
    C_id = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='C_id', related_name='loans')
    Amount = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.00'))
    Interest_rate = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    Type = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'Loan'

class Nominee(models.Model):
    N_id = models.AutoField(primary_key=True)
    C_id = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='C_id', related_name='nominees')
    N_Name = models.CharField(max_length=50)
    Relationship = models.CharField(max_length=50)
    DOB = models.DateField(blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Nominee'

class LoanStatusLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    C_id = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='C_id', related_name='loan_status_logs')
    L_id = models.ForeignKey('Loan', on_delete=models.CASCADE, db_column='L_id', related_name='status_logs')
    Type = models.CharField(max_length=25, blank=True, null=True)
    Status = models.CharField(max_length=50, blank=True, null=True)
    Start_date = models.DateField(blank=True, null=True)
    End_date = models.DateField(default='9999-12-31')
    Tot_Amount = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.00'))
    Cleared_Amount = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.00'))
    Updated_by = models.CharField(max_length=50, blank=True, null=True)
    Loan_purpose = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'LoanStatusLog'

    @property
    def Rem_Amount(self):
        return self.Tot_Amount - self.Cleared_Amount

class TransactionLog(models.Model):
    TRANSACTION_STATUS_CHOICES = [
        ('COMPLETED', 'Completed'),
        ('INPROCESS', 'In Process'),
        ('DISCARDED', 'Discarded'),
    ]

    T_id = models.AutoField(primary_key=True)
    Acc_id = models.ForeignKey('Account', on_delete=models.CASCADE, db_column='Acc_id', related_name='transactions')
    Amount = models.IntegerField()
    T_type = models.CharField(max_length=50)
    Timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS_CHOICES, default='INPROCESS')

    class Meta:
        db_table = 'TransactionLog'
