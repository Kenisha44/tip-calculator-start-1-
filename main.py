#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator!")
bill =float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
person = int(input("How many people to split the bill?\n"))
#Format the result to 2 decimal places = 33.60
bill_with_tip = tip/100 * bill + bill
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
bill_split = bill_with_tip/person
final_amount =round(bill_split,2)
final_amount= "{:.2f}".format(bill_split)
#Write your code below this line 👇
print(f"Each person should pay ${final_amount}.")