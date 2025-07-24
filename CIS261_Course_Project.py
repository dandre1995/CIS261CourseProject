""" Jack Dandre
 CIS261- Object Oriented Programming I
 Course Project Phase 1: Create and Call Functions with Parameters"""

from torch import Value


def get_employee_name():
     """Input and return the employees name"""
     while True:
         name = input("Enter employee name:").strip()
         if name:
             return name
         print("Name cannot be empty. Please try again.")
def get_total_hours():
    while True:
        try:
            hours = float(input("Enter total hours worked:"))
            if hours >= 0:
                return hours
            print("Hours must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def get_hourly_rate():
    while True:
        try:
            rate = float(input("Enter hourly rate:"))
            if rate >= 0:
                return rate
            print("Rate must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def get_tax_rate():
    while True:
        try:
            tax_rate = float(input("Enter income tax rate(as percentage):"))
            if 0 <= tax_rate <= 100:
                return tax_rate/100
            print("Tax rate must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def calculate_pay(hours, rate, tax_rate):
    gross_pay =hours*rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay
def display_employee_paystub(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    print("\nEmployee Pay Stub")
    print ("----------------------------")
    print(f"Name: {name}")
    print(f"Hours Worked:{hours:.2f}")
    print(f"Hourly Rate:${rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {tax_rate*100:.1f}%")
    print(f"Income Tax:${income_tax:.2f}")
    print(f"Net Pay:${net_pay:.2f}\n")
def display_summary_stats(employee_count,total_hours, total_gross, total_tax, total_net):
    print ("\nPayroll Summary")
    print("---------------------------")
    print(f"Total Employees:{employee_count}")
    print(f"Total Hours: {total_hours:.2f}")
    print(f"Total Gross Pay: ${total_gross:.2f}")
    print(f"Total Income Tax: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_net:.2f}")
def main():
    print("Employee Payroll System")
    print("Enter employee data or type 'End' to finish\n")

    employee_count = 0
    total_hours = 0.0
    total_gross = 0.0
    total_tax = 0.0
    total_net = 0.0

    while True:
        user_input = input("Press Enter to add employee or type 'End' to finish:").strip()
        if user_input.lower() =="end":
            break

        name = get_employee_name()
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        gross_pay, income_tax, net_pay = calculate_pay(hours, rate,tax_rate)
        display_employee_paystub(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay)

        employee_count +=1
        total_hours += hours
        total_gross += gross_pay
        total_tax += income_tax
        total_net += net_pay

        if employee_count >0:
            display_summary_stats(employee_count, total_hours, total_gross, total_tax, total_net)
        else:
            print("\n No employee data entered.")
if __name__ == "__main__":
    main()
