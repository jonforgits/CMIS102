# Jon Fabrycki // CMIS 102 // Date

# Function will create variables, then call the Welcome function.
# Function then will store 3 variables created from the Grade function
# Function will then store wtavggrade using the previously stored and created variables in the Grade Function
def main():

    bestgrade = 0 # Highest possible grade for all assignemnts
    bestgradename = ""
    names = ["Jon", "Melissa", "Emily", "Brad"] # Set student names
   
    # Inform user of what the program will do
    Welcome()
    
    # for each name in the names list the called functions will execute
    for name in names:
        discussion_grade, quiz_grade, assignment_grade = Grades(name)
        wtavggrade = WeightGrade(discussion_grade, quiz_grade, assignment_grade, name)
    
        bestgradename, bestgrade = BestGrade(wtavggrade, name, bestgrade, bestgradename)
    print("------------------------------------------------------------------------------")
    print("\nThe higest weighted grade is",bestgradename,"with a {:3.2f}%!".format(bestgrade),"\n")
    print("------------------------------------------------------------------------------\n")
# ----------------------------- Define functions ---------------------------------------

# Function will welcome the use and inform them what the program will do
# Should not return anything, just prints
def Welcome():
    print("\nThis is the assignment sum calculator.")
    print("Please utilize this calculator to find the highest grade of all the students!\n")
    
# Function will get the grade inputs for each assignment
# Return 3 variables that will need to be stored
def Grades(name):
    print("------------------------------------------------------------------------------")
    print("This grade input is for", name,"\n")
# Get all three grades
    discussion_grade = eval(input("Please enter the grade received on the discussion:  "))
    while discussion_grade < 0 or discussion_grade > 100: # Validate input
        print("Please enter a valid grade from 0 - 100")
        discussion_grade = eval(input("Please enter the grade received on the discussion:  "))
        
    quiz_grade = eval(input("Please enter the grade received on the quiz:  "))
    while quiz_grade < 0 or quiz_grade > 100: # Validate input
        print("Please enter a valid grade from 0 - 100")
        quiz_grade = eval(input("Please enter the grade received on the quiz:  "))
        
    assignment_grade = eval(input("Please enter the grade received on the assignment:  "))
    while assignment_grade < 0 or assignment_grade > 100: # Validate input
        print("Please enter a valid grade from 0 - 100")
        assignment_grade = eval(input("Please enter the grade received on the assignment:  "))
    
    return (discussion_grade, quiz_grade, assignment_grade)

# Function will get the weighted grade for a student
# Return a variable that will be used to check for highest score
def WeightGrade (discussion_grade, quiz_grade, assignment_grade, name):
    wtavggrade = discussion_grade * 0.15 + quiz_grade * 0.35 + assignment_grade * 0.5
    print("\nThe weighted grade for",name,"is: {:3.2f}%".format(wtavggrade))
    return wtavggrade


# Function will take the weighted average grade and compare it to the current best grade
# Returns a new best grade and the name that had the best grade is then created as bestgradename
def BestGrade(wtavggrade, name, bestgrade, bestgradename):
    if (wtavggrade > bestgrade):
        bestgrade = wtavggrade
        bestgradename = name # name of student with best average grade

    return bestgradename, bestgrade

# -------------- Execute main function ----------------------
main()
