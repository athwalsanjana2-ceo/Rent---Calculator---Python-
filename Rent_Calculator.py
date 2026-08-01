try:
    rent = int(input("Enter your hostel/flat rent = "))
    food = int(input("Enter the amount of food ordered = "))
    electricity_spend = int(input("Enter the total of electricity spend = "))
    charge_per_unit = int(input("Enter the charge per unit = "))
    persons = int(input("Enter the number of persons living in room/flat = "))

    total_bill = electricity_spend * charge_per_unit
    per_person = (food + rent + total_bill) / persons

    print(f"\nEach person will pay = {per_person:.2f}")

except ZeroDivisionError:
    print("Persons 0 nahi ho sakte bhai!")
except ValueError:
    print("Please number hi enter karo!")
