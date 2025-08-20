""" Jack Dandre
 CIS261- Object Oriented Programming I
 Course Project Phase 1: Create and Call Functions with Parameters
 Course Project Phase 2: Using Lists and Dictionaries to store and retreive data"""


import re
from datetime import datetime

def validate_date(date_str):
    """Validate date format mm/dd/yyyy"""
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$'
    if re.match(pattern, date_str):
        try:
            datetime.strptime(date_str, '%m/%d/%Y')
            return True
        except ValueError:
            return False
    return False

def get_date_range():
    while True:
        from_date = input("Enter from Date (mm/dd/yyyy): ").strip()
        to_date = input("Enter to Date (mm/dd/yyyy): ").strip()

        if validate_date(from_date) and validate_date(to_date):
            return from_date, to_date
        print("Invalid date format. Please use mm/dd/yyyy format with valid dates.\n")

def get_employee_name():
    """Input and return the employee's name"""
    while True:
        name = input("Enter employee name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")

def get_total_hours():
    while True:
        try:
            hours = float(input("Enter total hours worked: "))
            if hours >= 0:
                return hours
            print("Hours must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_hourly_rate():
    while True:
        try:
            rate = float(input("Enter hourly rate: "))
            if rate >= 0:
                return rate
            print("Rate must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_tax_rate():
    while True:
        try:
            tax_rate = float(input("Enter income tax rate (as percentage): "))
            if 0 <= tax_rate <= 100:
                return tax_rate / 100
            print("Tax rate must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_paystub(from_date, to_date, name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    print("\nEmployee Pay Stub")
    print("----------------------------")
    print(f"Pay Period: {from_date} to {to_date}")
    print(f"Name: {name}")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {tax_rate * 100:.1f}%")
    print(f"Income Tax: ${income_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}\n")

def save_employee_data(filename, employee_data):
    """Save employee data to file in pipe-delimited format"""
    with open(filename, 'a') as file:
        record = f"{employee_data['from_date']}|{employee_data['to_date']}|{employee_data['name']}|"
        record += f"{employee_data['hours']}|{employee_data['rate']}|{employee_data['tax_rate']}\n"
        file.write(record)

def generate_report(filename):
    """Generate payroll report based on user input"""
    while True:
        report_date = input("\nEnter From Date for report (mm/dd/yyyy) or 'All' for all records: ").strip()
        
        if report_date.lower() == 'all':
            break
        elif validate_date(report_date):
            break
        else:
            print("Invalid date format. Please use mm/dd/yyyy format or 'All'.")
    
    # Initialize totals
    totals = {
        'employee_count': 0,
        'total_hours': 0.0,
        'total_gross': 0.0,
        'total_tax': 0.0,
        'total_net': 0.0
    }
    
    print("\nPayroll Report")
    print("=" * 80)
    print(f"{'From Date':<12} {'To Date':<12} {'Employee Name':<20} {'Hours':>6} {'Rate':>8} {'Gross':>10} {'Tax Rate':>8} {'Tax':>8} {'Net':>10}")
    print("-" * 80)
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) != 6:
                    continue
                
                from_date, to_date, name, hours_str, rate_str, tax_rate_str = data
                
                # Check if this record should be included in the report
                if report_date.lower() != 'all' and from_date != report_date:
                    continue
                
                # Convert string data to appropriate types
                try:
                    hours = float(hours_str)
                    rate = float(rate_str)
                    tax_rate = float(tax_rate_str)
                except ValueError:
                    continue
                
                # Calculate pay
                gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
                
                # Update totals
                totals['employee_count'] += 1
                totals['total_hours'] += hours
                totals['total_gross'] += gross_pay
                totals['total_tax'] += income_tax
                totals['total_net'] += net_pay
                
                # Display employee record
                print(f"{from_date:<12} {to_date:<12} {name:<20} {hours:>6.1f} {rate:>8.2f} {gross_pay:>10.2f} {tax_rate*100:>7.1f}% {income_tax:>8.2f} {net_pay:>10.2f}")
    
    except FileNotFoundError:
        print("No employee data found.")
        return
    
    # Display totals
    print("-" * 80)
    print(f"{'TOTALS:':<46} {totals['total_hours']:>6.1f} {'':>8} {totals['total_gross']:>10.2f} {'':>8} {totals['total_tax']:>8.2f} {totals['total_net']:>10.2f}")
    print(f"{'Number of employees:':<46} {totals['employee_count']:>6}")
    print("=" * 80)

def main():
    print("Employee Payroll System")
    print("Enter employee data or type 'End' to finish\n")
    
    filename = "employees.txt"
    
    # Data entry loop
    while True:
        user_input = input("Press Enter to add employee or type 'End' to finish: ").strip()
        if user_input.lower() == "end":
            break
        
        from_date, to_date = get_date_range()
        name = get_employee_name()
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        
        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
        
        # Create employee record
        employee_data = {
            'from_date': from_date,
            'to_date': to_date,
            'name': name,
            'hours': hours,
            'rate': rate,
            'tax_rate': tax_rate,
            'gross_pay': gross_pay,
            'income_tax': income_tax,
            'net_pay': net_pay
        }
        
        # Save to file
        save_employee_data(filename, employee_data)
        
        # Display pay stub
        display_employee_paystub(from_date, to_date, name, hours, rate, gross_pay,
                                 tax_rate, income_tax, net_pay)
    
    # Generate report
    generate_report(filename)

if __name__ == "__main__":
    main()
