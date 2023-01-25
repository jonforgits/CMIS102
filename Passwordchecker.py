# Jon // CMIS 102 // Date
# Password must contain at least 1 digit and 1 alphabetic character
# Password must not contain any spaces and must be between 10 - 20 characters


def main():
    Welcome()
    pwd = input("\nPlease type in a password:  ")# Get users password
    print("\n")
    
    if CheckLength(pwd) and CheckNandD(pwd) and ValidChars(pwd) is True: # If all functions return True print Password is valid
        print("""
------------------------------------------------------------------------------------------------
                        The password you entered is valid!
------------------------------------------------------------------------------------------------
        """)
    


# --------------------------- Functions ---------------------------
# Function will inform user what program will do and inform them of the requirements
def Welcome():
    print("""----------------------------------------------------------------------------------\n
    Welcome to the most secure password creator in the world!
    We will evaluate your password and ensure it meets all requirements.\n
-------------------------------------------------------------------------------------------\n
    Your password must be between 10 and 20 characters.
    Your password must contain at least 1 alphabetic charcater AND at least 1 digit.
    Your password must NOT contain any spaces.\n"""
        )
    print("----------------------------------------------------------------------------------")

# Function will take the input password and check it for length - must be greater than 10 but less than 20
def CheckLength(pwd):
    if len(pwd) < 10: # Validate the password is long enough
        reason = "Not long enough!\nPassword needs to be between 10 and 20 characters"
        Reprompt(reason)
    elif len(pwd) > 20: # Validate the password is not too long
        reason = "Too long!\nPassword needs to be between 10 and 20 characters"
        Reprompt(reason)
    else: 
        return True

# Function will take the input password and check it to ensure it has the proper number of characters 
# AND at least 1 digit and 1 alphabetic character
def CheckNandD(pwd):
    if (pwd.isdigit()): # Check if the password is all digits
        reason = "Password needs to contain at least 1 alphabetic charcater"
        Reprompt(reason)
    elif (pwd.isalpha()): # Check if password is all alphabetic characters
        reason = "Password needs to contain at least 1 digit"
        Reprompt(reason)
    else:
        return True
    
# Function will check the password to ensure there are no prohibited characters (space is prohibited)
# Return true if there are no spaces used   
def ValidChars(pwd):
    for char in pwd:
        if char == ' ':
            reason = "\nInvalid, there should be no spaces."
            Reprompt(reason)
    return True
    
# Function will print the reason for being called and then prompt the user for a new password
# Function will then check that each function returnrs True to validate the password meets the requirements
def Reprompt(reason):
    print(reason,"\n")
    pwd = input("\nPlease enter a password that meets the requirements:  ")
    if CheckLength(pwd) and CheckNandD(pwd) and ValidChars(pwd) is True:
        print("The password you entered is valid!\n")
    

main()
