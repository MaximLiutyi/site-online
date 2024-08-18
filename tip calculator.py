print("Welcome to tip calculator!")
bil = float(input("What was the total bill? $"))
tip = int(input("How much would you like yo give? 10, 12, or 15? "))
people = int(input("How many people yo split the bill?"))
tip_as_percent = (tip / 100 * bil + bil)
bill_per_person = tip_as_percent / people
final_amount = round(bill_per_person, 2)
print(f"Кожен має сплатити по: ${final_amount}")


