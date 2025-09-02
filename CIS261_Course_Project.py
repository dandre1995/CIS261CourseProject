""" Jack Dandre
 CIS261- Object Oriented Programmin I
 Course Project Phase 1: Create and Call Functions with Parameters
 Course Project Phase 2: Using Lists and Dictionaries to store and retreive data
 Couse Project Phase 3: Creating, L\Listing and Retrieving files
 Course Project Phase 4: Add Basic Security  to the Application """
import re
from datetime import datetime

class Login:
    """Class to handle user authentication with three properties: User ID, Password, and Authorization"""
    
    def __init__(self, user_id="", password="", authorization=""):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

def create_login_file():
    """Create and populate the login file with user information"""
    login_data = [
        "admin|adminpass|Admin",
        "user1|userpass|User",
        "user2|pass123|User"
    ]
    
    try:
        with open("login.txt", "w") as file:
            for record in login_data:
                file.write(record + "\n")
    except IOError:
        print("Error creating login file.")

def validate_user_input(user_id, password):
    """Validate that user ID and password are not empty and meet basic requirements"""
    if not user_id or not user_id.strip():
        return False, "User ID cannot be empty."
    
    if not password or not password.strip():
        return False, "Password cannot be empty."
    
    return True, "Valid input."

def login_process():
    """Handle the login process and return Login object with user information"""
    login_user = Login()
    
    # Open and read login file
    try:
        with open("login.txt", "r") as file:
            login_records = []
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    login_records.append({
                        'user_id': parts[0],
                        'password': parts[1], 
                        'authorization': parts[2]
                    })
    except FileNotFoundError:
        print("Login file not found. Creating default login file...")
        create_login_file()
        return login_process()  # Retry after creating file
    
    # Get user input
    while True:
        user_id = input("Enter User ID: ").strip()
        password = input("Enter Password: ").strip()
        
        # Validate input
        is_valid, message = validate_user_input(user_id, password)
        if not is_valid:
            print(message)
            continue
        
        # Check if user exists in records
        user_found = False
        for record in login_records:
            if record['user_id'] == user_id:
                user_found = True
                if record['password'] == password:
                    # Successful login
                    login_user.user_id = user_id
                    login_user.password = password
                    login_user.authorization = record['authorization']
                    print(f"Login successful! Welcome {user_id}")
                    return login_user
                else:
                    print("Invalid password. Please try again.")
                    break
        
        if not user_found:
            print("User ID does not exist. Please try again.")

def display_user_info(login_obj):
    """Display user ID, password, and authorization for all users"""
    print("\nUser Information:")
    print("-" * 40)
    print(f"User ID: {login_obj.user_id}")
    print(f"Password: {login_obj.password}")
    print(f"Authorization: {login_obj.authorization}")
    print("-" * 40)

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
    print("Employee Payroll System - Login Required")
    print("=" * 50)
    
    # Handle login process first
    current_user = login_process()
    
    # Display user information after successful login
    display_user_info(current_user)
    
    # Check authorization and modify functionality accordingly
    if current_user.authorization == "Admin":
        print("Admin access granted - Full functionality available")
        can_enter_data = True
        can_display_data = True
    elif current_user.authorization == "User":
        print("User access granted - Display data only")
        can_enter_data = False
        can_display_data = True
    else:
        print("Unknown authorization level")
        can_enter_data = False
        can_display_data = False
    
    filename = "employees.txt"
    
    # Data entry loop (only for Admin users)
    if can_enter_data:
        print("\nEnter employee data or type 'End' to finish\n")
        
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
    
    # Generate report (available for both Admin and User)
    if can_display_data:
        generate_report(filename)
    
    print("\nThank you for using the Employee Payroll System!")

if __name__ == "__main__":
    main()
