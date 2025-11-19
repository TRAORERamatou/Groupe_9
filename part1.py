print("*************************WELCOME****************************************")
print("*************************to*********************************************")
print("*************************Python Project*********************************")
print("***********************************************************************")
print("*************************STUDENT PROFILES & FEE SUMMARY**********")

# All of inputs are taken from user

full_name = str(input("Enter your fullname: "))
student_id = int(input("Enter your student ID : "))
field = str(input("Enter your field: "))
age = int(input("Enter your age: "))
year_of_study = int(input("Enter your current year_of_study: "))
credit_number = int(input("Enter the number of credits you registered: "))
price_per_credit = float(input("Enter the price-per-credit: "))
registration_fees = float(input("Enter your registration fees: "))
scholarship = input("Have you a scholarship? (True or False): ")
current_level = input("Current level (eg: L1, L2, ...) : ")
tuition_fee = float(input(f"\nTuition fee for {current_level} (eg: 500000 FCFA) : "))
other_fees = float(input("Other fees (eg:library, medical...)   : "))
scholarship_pct= float(input("Scholarship percentage (0 if none) : "))
amount_paid = float(input("Amount already paid (in FCFA)   : "))


# Calculations

total_gross = tuition_fee + other_fees                                    
scholarship_amount = total_gross * (scholarship_pct / 100)                     
net_after_scholarship = total_gross - scholarship_amount                        
remaining_balance= net_after_scholarship - amount_paid

#output the results 
 
# Student Profile
print("\n************STUDENT PROFILE************")                      
print(f"Your full name is {full_name}, you are {age} years old.")
print(f"Your id is {student_id}")
print(f"Your field is {field}")
print("year of study: ",year_of_study)
print("Your credit number: ",credit_number)
print("Your price per credit: ",price_per_credit)
print("Your resisgtration fee is: ",registration_fees)
print("Your sclolarship is: ",scholarship)
print("Your sclolarship amount is: ",scholarship_amount)

print("\n************FEE SUMMARY************")

print(f"Gross tuition fees : {total_gross:} FCFA")
print(f"Scholarship ({scholarship_pct:}%)-{ scholarship_amount:} FCFA")
print(f"Net after scholarship : {net_after_scholarship:} FCFA")
print(f"Amount already paid : {amount_paid:} FCFA")
print(f"REMAINING BALANCE : {remaining_balance:} FCFA")


