#Logan Nelson
#12/18
#Tic_Tac_Toe against computer

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#functions
def display_instructions():
    """Display game instructions."""
    print(
        """
            Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
            This will be a showdown between your human brain and my silicon processor.

            You will make your move known by entering a number,0-8. The number
            will correspond to the board position as illustrated:

    
       0  |  1   | 2
   -------|------|-----
       3  |   4  | 5
   -------|------|-----
      6   |   7  | 8

          Prepare yourself""")

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question+" y or n").lower()
    return response
##    
##        answer = input()
##        while answer.lower() != "y" or "n"
##        if answer== "n":
##            return "No"
##        elif answer== "y":
##            return "Yes"
##        else:
##            print(answer)

display_instructions()
x=ask_yes_no("do you hate this class")
print (x)

def ask_num(question, low, high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")
            response = input(question)
    return int(response)

x=ask_num("enter a number between 1 and 10 ",1,11)
print (x)
    
    
    
