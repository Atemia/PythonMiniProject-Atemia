#!/usr/bin/python

"""Functions Runs a software analyzer fro pdb files using tools from pdbSoftwareTools
"""
def mainMenu():
    """Function: Runs the software by calling various defined functions for the different options and also the display of the software"""
    import sys
    import pdbSoftwareTools
    red = lambda text: '\033[0;31m' + text + '\033[0m'
    
    global file
    file= "None"
    menu()                                              # The display function
    
    def choiceMenu():
        """Function: allows the diffrent options from the defined function to be accesed at any given time while running the software"""
        
        if choice.lower()== ("i"):                      #
            choiceI()                       
            choiceMenu()
        if choice.lower() == ("h"):
            choiceH()
            choiceMenu()
        if choice.lower() == ("s"):
            choiceS(load_file)
            choiceMenu()
        if choice.lower()== ("x"):                      #
            choiceX()
            choiceMenu()
        else:
            if choice.lower() == "o":
                print("Current loaded pdb file is %s"%red(load_file),"\nDo you want to load another file (yes/no)")
                key = input()
                if key.lower() == 'yes':
                    mainMenu()
                elif key.lower() == "no":
                    pass
                    menu()
                    choiceMenu()
                    
            if choice.lower() == "q":
                print(red("Do you want to exit(E) or do you want go back to the menu (M)"))
                select = input()
                if select.lower() == "e":
                    sys.exit(red("Good bye! Thank you for using this sofware."))
                elif select.lower() == "m":
                    mainMenu()
                    
            if choice.lower() not in ('o', 'i', 'h', 's', 'x', 'q'):
                print(red("Invalid option selected"))
                menu()
                mainMenu()

    if choice.lower() in ('o', 'i', 'h', 's', 'x', 'q'):
        if choice.lower() == "o":
            choiceO()
            choiceMenu()

        if choice.lower() == "q":
            print(red("Do you want to exit(E) or do you want go back to the menu (M)"))
            select = input()
            if select.lower() == "e":
                sys.exit(red("Good bye! Thank you for using this sofware."))
            elif select.lower() == "m":
                mainMenu()         
    else:
        print(red("Invalid choice!\nEnter a valid choice ie 'o' to load a pdb file or 'q' to Exit the program "))
        mainMenu()

mainMenu()
