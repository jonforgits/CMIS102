# Main function to get input from user
def main():
   print("\nLet's see how much money you made this week!\n")
   paperperday = int(input("How many papers did you deliver each day?   "))
   daysdelivered = int(input("How many days did you delivery paper this week?   ")) 
   tips = float(input("How much money did you recieve in tips this week?    "))
   
   # Constant values
   newspaper = 5 # Newspapers will cost $5
   commissionpercent = .05 # Commission will be 5% or 25 cents or multiplied by .05
   
   commission = newspaper  * commissionpercent # Commision per paper
   papersdelivered = paperperday * daysdelivered # Papers Delivered Weekly
   weeklysalary = commission * papersdelivered # Weekly salary based off commissions
   
   totalsales = weeklysalary + tips # Total amount made for the week with tips
   
   print("-------------------------------------------------------")
   
   # Total number of papers delivered in the week
   print("\nYou delivered", papersdelivered, "papers this week!")
   
   # Print weekly salary without tips
   print("\nYour weekly salary was: $",weeklysalary)
   
   # Print toal salary with tips
   print("\nWith tips you made a grand total of $",totalsales, "this week!\n")    
   
   print("-------------------------------------------------------")
   # Execute
main()

