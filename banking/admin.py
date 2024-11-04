from django.contrib import admin
from .models import Bank, Branch, Employee, Customer, Account, Loan, Nominee, LoanStatusLog, TransactionLog

admin.site.register(Bank)
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(Nominee)
admin.site.register(LoanStatusLog)
admin.site.register(TransactionLog)
