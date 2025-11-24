# ============================================================
# Student Fee Calculator + Simple CLI Student Management

# ============================================================

students = []

# --------------------------
# SAFE INPUT FUNCTIONS
# --------------------------

def input_int(msg, minimum=None, maximum=None):
    """Input sécurisé pour les entiers."""
    while True:
        try:
            value = int(input(msg).strip())
            if minimum is not None and value < minimum:
                print(f"Value must be >= {minimum}")
                continue
            if maximum is not None and value > maximum:
                print(f"Value must be <= {maximum}")
                continue
            return value
        except ValueError:
            print("Enter a valid number.")

def input_float(msg, minimum=None):
    """Input sécurisé pour les nombres décimaux."""
    while True:
        try:
            value = float(input(msg).strip())
            if minimum is not None and value < minimum:
                print(f"Value must be >= {minimum}")
                continue
            return value
        except ValueError:
            print("Enter a valid number.")

def input_bool(msg):
    """Convertit True/False à partir du texte utilisateur."""
    while True:
        val = input(msg).strip().lower()
        if val in ["true", "yes", "y", "1"]:
            return True
        if val in ["false", "no", "n", "0"]:
            return False
        print("Enter True or False.")

# --------------------------
# FEE CALCULATION
# --------------------------

def calculate_fees(tuition_fee, other_fees, scholarship_pct, amount_paid):
    total_gross = tuition_fee + other_fees
    scholarship_amount = total_gross * (scholarship_pct / 100)
    net_after_scholarship = total_gross - scholarship_amount
    remaining_balance = net_after_scholarship - amount_paid
    return total_gross, scholarship_amount, net_after_scholarship, remaining_balance

# --------------------------
# SIMPLE CALCULATOR
# --------------------------

def run_simple_calculator():
    print("\n===== SIMPLE CALCULATOR =====")

    full_name = input("Full name: ").strip()
    student_id = input_int("Student ID (number): ", minimum=1)
    age = input_int("Age: ", minimum=1)
    field = input("Field: ").strip()

    year_of_study = input_int("Year of study: ", minimum=1)
    credit_number = input_int("Credit number: ", minimum=0)
    price_per_credit = input_float("Price per credit: ", minimum=0)
    registration_fees = input_float("Registration fees: ", minimum=0)

    has_scholarship = input_bool("Do you have a scholarship? (True/False): ")

    level = input("Level (L1, L2…): ").strip()
    tuition_fee = input_float("Tuition fee: ", minimum=0)
    other_fees = input_float("Other fees: ", minimum=0)

    scholarship_pct = 0
    if has_scholarship:
        scholarship_pct = input_float("Scholarship percentage: ", minimum=0)

    amount_paid = input_float("Amount already paid: ", minimum=0)

    # Final calculation
    total_gross, scholarship_amount, net_after_scholarship, remaining_balance = \
        calculate_fees(tuition_fee, other_fees, scholarship_pct, amount_paid)

    print("\n===== RESULT =====")
    print(f"Gross fees: {total_gross} FCFA")
    print(f"Scholarship: {scholarship_amount} FCFA")
    print(f"Net after scholarship: {net_after_scholarship} FCFA")
    print(f"Amount paid: {amount_paid} FCFA")
    print(f"Remaining balance: {remaining_balance} FCFA")

# --------------------------
# ADD STUDENT TO MEMORY
# --------------------------

def add_student_interactive():
    print("\n=== ADD STUDENT ===")

    full_name = input("Full name: ").strip()
    student_id = input_int("Student ID: ", minimum=1)
    field = input("Field: ").strip()
    age = input_int("Age: ", minimum=1)
    year_of_study = input_int("Year of study: ", minimum=1)
    level = input("Level (L1, L2…): ").strip()

    credit_number = input_int("Number of credits: ", minimum=0)
    price_per_credit = input_float("Price per credit: ", minimum=0)
    registration_fees = input_float("Registration fees: ", minimum=0)

    has_scholarship = input_bool("Scholarship (True/False): ")
    scholarship_pct = 0
    if has_scholarship:
        scholarship_pct = input_float("Scholarship percentage: ", minimum=0)

    tuition_fee = input_float("Tuition fee: ", minimum=0)
    other_fees = input_float("Other fees: ", minimum=0)
    amount_paid = input_float("Amount paid: ", minimum=0)

    total_gross, scholarship_amount, net_after_scholarship, remaining_balance = \
        calculate_fees(tuition_fee, other_fees, scholarship_pct, amount_paid)

    student = {
        "full_name": full_name,
        "id": student_id,
        "field": field,
        "age": age,
        "year_of_study": year_of_study,
        "level": level,
        "credit_number": credit_number,
        "price_per_credit": price_per_credit,
        "registration_fees": registration_fees,
        "has_scholarship": has_scholarship,
        "scholarship_pct": scholarship_pct,
        "tuition_fee": tuition_fee,
        "other_fees": other_fees,
        "amount_paid": amount_paid,
        "total_gross": total_gross,
        "scholarship_amount": scholarship_amount,
        "net_after_scholarship": net_after_scholarship,
        "remaining_balance": remaining_balance,
    }

    students.append(student)
    print(f"Student '{full_name}' added successfully!")

# --------------------------
# VIEW STUDENTS
# --------------------------

def list_students():
    print("\n=== STUDENT LIST ===")
    if not students:
        print("No students registered.")
        return
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['full_name']} - Remaining: {s['remaining_balance']} FCFA")

def student_details():
    if not students:
        print("No students available.")
        return

    idx = input_int(f"Choose student (1-{len(students)}): ", minimum=1, maximum=len(students))
    s = students[idx - 1]

    print("\n=== DETAILS ===")
    for key, value in s.items():
        print(f"{key}: {value}")

# --------------------------
# MAIN MENU
# --------------------------

def main_menu():
    while True:
        print("""
===== MENU =====
1. Use simple calculator
2. Add student
3. List students
4. View student details
5. Quit
""")
        choice = input("Choice: ").strip()

        if choice == "1":
            run_simple_calculator()
        elif choice == "2":
            add_student_interactive()
        elif choice == "3":
            list_students()
        elif choice == "4":
            student_details()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
