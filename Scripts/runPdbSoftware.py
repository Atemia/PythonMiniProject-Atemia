# FUNCTIONS/SOFTWARE TOOLS

## MAIN DISPALY MENU
   

def menu():
    """
    Function: Displays the menu with different options for the user
    Arguments: None
    Returns: Menu
    
    """
    blue = lambda text: '\033[0;34m' + text + '\033[0m' # Colors the printed output blue
    red = lambda text: '\033[0;31m' + text + '\033[0m'
    software = "PDB FILE ANALYZER"
    choices = "Select an option from below:"
    c1 = "1) Open a PDB file                     (O)"
    c2 = "2) Information                         (I)"
    c3 = "3) Show histrogram of amino acids      (H)"
    c4 = "4) Display Secondary Structure         (S)"
    c5 = "5) Export PDB File                     (X)"
    c6 = "6) Exit                                (Q)"
    global file
    status = "Current PDB: "+ file
    len(software)

    stars="*"
    space=" "
    print(blue(stars*80))
    #The length of the inserted string and its 0 index is subtracted for the desired 80 characters per line to be met.
    #Subtract index 0s in each object added, this concept is applied to each line.
    print(blue(stars * 1),blue("%0s"%""),blue("%s"%software),space*(75-(len(software)))+blue(stars))
    print(blue(stars*80))
    print(blue(stars * 1),"%0s"%"",blue("%s" %choices),space*(75-(len(choices)))+blue(stars) ) 
    print(blue(stars*1), blue(space*76), blue(stars*1))
    print(blue(stars * 1),"%5s"%"",blue("%s" %c1),space*(70-(len(c1)))+blue(stars))
    print(blue(stars * 1),"%5s"%"",blue("%s"%c2),space*(70-(len(c2)))+blue(stars))
    print(blue(stars * 1),"%5s"%"",blue("%s" %c3),space*(70-(len(c3)))+blue(stars))
    print(blue(stars * 1),"%5s"%"",blue("%s" %c4),space*(70-(len(c4)))+blue(stars))
    print(blue(stars * 1),"%5s"%"",blue("%s" %c5),space*(70-(len(c5)))+blue(stars))
    print(blue(stars * 1),"%5s"%"",blue("%s" %c6),space*(70-(len(c6)))+blue(stars))
    print(blue(stars * 1),"%0s"%"",space*(74-(len(status))),blue("%s" %status),blue(stars*1))
    print(blue(stars*80))
    global choice
    choice = input(":")    

# PDB FILE FORMART TESTING

def fungua(filename):
    """
    Function: Opens and tests a valid file path by loading it to the memory 
              Test if the file is a pdb file
    Argument: Name or valid path of the file
    
    """
    red = lambda text: '\033[0;31m' + text + '\033[0m'
    
    from pathlib import Path
    filename = Path(filename)    
    try:
        with open(filename, 'r') as f:
            global file 
            file = filename.name
            checkList= ['HEADER','OBSLTE','TITLE','SPLT','CAVEAT','COMPND','SOURCE','KEYWDS','EXPDTA','NUMMDL','MDLTYP',\
        'AUTHOR','REVDAT','SPRSDE','JRNL','REMARKS','DBREF','DBREF1','DBREF2','SEQADV','SEQRES','MODRES',\
        'HET','FORMUL','HETNAM','HETSYN','HELIX','SHEET','SSBOND','LINK','CISPEP','SITE','CRYST1','MTRIXn',\
        'ORIGXn','SCALEn','MODEL','ATOM','ANISOU','TER','HETATM','ENDMDL','CONECT','MASTER','END']
            checkList = ','.join(checkList)
            for line in f:
                if len(line) == 81:
                    pass
                    starts = str(line[:6])
                    status = True
                    for i in starts:
                        if i in checkList:
                            pass
                        else:
                            status = False
                    return status
    except:
            print(red("Invalid file loaded."))
            
## CHOICES OPTIONS
def choiceO():
    """Function: loads the file to the software"""
    red = lambda text: '\033[0;31m' + text + '\033[0m'
    global load_file        # Retains the loaded file the memory of the software allowing other functions to open the file using this variable
    load_file = str(input('Enter a Valid PATH for a PDB File:'))
    if fungua(load_file) == True:
        try:
            print(red("The File %s has been sucessfully loaded" %load_file))
        except:
            print(red("Ivalid file loaded"))
            global file        #Displays the name of the file on the menu as long as it is loaded
            file = "None"
    else:
        print(red("The file loaded does not follow the pdb format.\nPlease Enter a valid  pdb file"))
        menu()
        choiceO()
    menu()
    
    
# CHOICES INFORMATION
def choiceI():
    """Function prints a summary of the general description of the pdb file"""
    titlePdb() # prints the file name and the title of th pdb file
    printChains(load_file)
    chainInfo(load_file)
    menu()

##
def titlePdb():
    """
    Function: Extracts the title from the pdb file.
    
    """
    from pathlib import Path
    red = lambda text: '\033[0;31m' + text + '\033[0m'
    if fungua(load_file):
        myLis = []
        myFile = Path(load_file)
        with open(load_file, 'r') as f:
            global file 
            file = myFile.name
            print("PDB File: %s " %red(file) )
            Title = ""
            for line in f:
                if line.startswith('TITLE'):
                    Title = line.strip('TITLE')
                    Title = Title.strip()
                    myLis.append(Title)
            myString = str(("").join(myLis)) # joining the list and converting it into a string
            myString = "Title: " + myString.strip()
            if len(myString) <= 80:
                print(myString[:80])
            else:
                print(myString[:80]+"\n"+myString[80:])

##
def printChains(load_file):
    """ 
    Input: pdb file
    Function: Prints all the chains in the pdb file
    """
    with open(load_file, 'r') as f:
        chain = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        lyst = ""
        for line in f:
            if line.startswith('SEQRES'):
                s = line.split()[2:]         # creaeting a list of our three letter code amino acids and displays starting from the chain type
                for i in s:
                    for letter in chain:
                        if i == letter:
                            lyst+= letter
        lyst = sorted(lyst)             #sort the list
        lyst = list(dict.fromkeys(lyst)) # remove duplicates leaving us with the number of chains in the pdb file
        lyst = "".join(lyst)
        global chainString
        chainString = str(lyst[:-1])+str(lyst[-1])
        allChains = str(lyst[:-1])+' '+'and'+' '+str(lyst[-1])
        print('Chains: '+ allChains)
        
##
def chainInfo(load_file):

    import textwrap # introduces prints stirng of specified length

    aa_dic = {'A':'ALA', 'R':'ARG', 'N':'ASN', 'D':'ASP', 'G':'GLY', 'Q':'GLN', 'E':'GLU', 'H':'HIS','C':'CYS',\
              'I':'ILE', 'L':'LEU', 'K':'LYS', 'M':'MET', 'F':'PHE', 'P':'PRO', 'S':'SER', 'T':'THR', 'W':'TRP', 'Y':'TYR', 'V':'VAL'} # dictionary for amino acids
    new_dict = dict([(value, key) for (key, value) in aa_dic.items()]) # swapped the values and keys 


    def no_aa(seq):
        """Input: amino acid sequence
           Fuinction: number of amino acids in a chain   
        """
        return (len(seq)-(len(seq)//50))

    def getHelixNos(chain):
        """Input: chain name e.g "A", "B" ...
           Function: counts the number of helices in a chain
        """
        with open(load_file, 'r') as f:
            h = ""
            for line in f:
                if line.startswith('HELIX'):
                    l = line.split()[4:]
                    if l[0] == chain:
                        h += l[0]
            return (len(h))


    def getSheetNos(chain):
        """Input: chain name e.g "A", "B" ...
           Function: counts the number of sheets in a chain
        """
        with open(load_file, 'r') as f:
            sh = "" 
            for line in f:
                if line.startswith('SHEET'):
                    l = line.split()[5:]
                    if l[0] == chain:
                        sh += l[0]
            return (len(sh))


    with open(load_file, 'r') as f:
        chains = []
        for line in f:
            if line.startswith('SEQRES'):
                l = line.split()[2:]         # creaeting a list of our three letter code amino acids and displays starting from the chain type
                chains.append(l[0])
                chains = (list(dict.fromkeys(chains)))

        for i in chains:
            seq = ""
            with open(load_file, 'r') as f:
                for line in f:
                    l = line.split()
                    if line.startswith('SEQRES')and i == l[2]:
                        l = l[4:]
                        c = [new_dict[codon]for codon in l]
                        seq += "".join(c)
            space = " "
            s = ("\n"+space*15).join(textwrap.wrap(seq,50))
            print(" - Chain %s" % i)
            print("%4s Number of amino acids: "%"",no_aa(seq))
            print("%4s Number of helix: %9d"%("",getHelixNos(i)))
            print("%4s Number of sheet: %9d"%("",getSheetNos(i)))
            print("%4s Sequence: %s" % ("",s))
            
# Choice H  - Amino acids histograms

def choiceH():
    red = lambda text: '\033[0;31m' + text + '\033[0m'
    options()
    if option.lower() in ('an', 'dn', 'aa', 'da'):
        selectionOutput(option,load_file)
    else:
        print(red("Please enter a valid option"))
        choiceH()
##
def options():
    blue = lambda text: '\033[0;34m' + text + '\033[0m'
    print(blue("Choose an option to order by:"))
    print(blue("   number of amino acids - ascending  (an)"))
    print(blue("   number of amino acids - descending (dn)"))
    print(blue("   alphabetically - ascending         (aa)"))
    print(blue("   alphabetically - descending        (da)"))
    global option
    option = input("Order by:")

##
def selectionOutput(option,load_file):
    """
        Input: options on the display i.e. an', 'dn', 'aa' and 'da'
        Function: prints a summary of the amino acids in a pdb files according to the number of times an amino acid is in the sequence
    """
    with open(load_file, 'r') as f:
        seq = []
        for line in f:
            if line.startswith('SEQRES'):
                l = line.split()[4:]       # creaeting a list of our three letter code amino acids and displays starting from the chain type
                seq += l
    sL = []
    dic = dict()
    for i in seq:
        sL.append(i)
    for aa in sL:
        dic[aa] = dic.get(aa,0) + 1

    if option.lower() == 'aa':
        # Alphabetically sorted amino acid histograms aa (ascending)
        sort_Aa_dic = (dict(sorted(dic.items(), key = lambda t : t[0])))
        sortedDic = dict(sort_Aa_dic)
        for k,v in sortedDic.items():
            print(k, "( %2d)" %v,": "+"*"*v)

    elif option.lower() =="da":
        # Alphabetically sorted amino acid histograms da (descending)
        sort_Aa_dic = (dict(sorted(dic.items(), key = lambda t : t[0], reverse = True)))
        sortedDic = dict(sort_Aa_dic)
        for k,v in sortedDic.items():
            print(k, "( %2d)" %v,": "+"*"*v)
    elif option.lower() =="dn":
        # choice dn decending ( by number of amino acids)
        sort_no_aa_dic = (sorted(dic.items(), key = lambda t : t[1]))
        s = dict(sort_no_aa_dic)

        for k,v in s.items():
            print(k, "( %2d)" %v,": "+"*"*v)
    
    elif option.lower() =="an":
        # choice an acending ( by number of amino acids)
        sort_no_aa_dic = (sorted(dic.items(), key = lambda t : t[1], reverse = True))
        s = dict(sort_no_aa_dic)

        for k,v in s.items():
            print(k, "( %2d)" %v,": "+"*"*v)
    else:
        print("Invalid selection made! Try again")
    menu()

# CHOICE S
def choiceS(load_file):    
    """Input: pdb file
       Functions: displays the secondary structure of a pdb file
    """
    print("Secondary Structure of the PDB id %s"%load_file)                        
    def seq_helix_sheet3D(load_file, seq, chain):

        """Input: pdb file, sequence of a particular chain from the pdb, the chain name of the sequence eg "A","B","P" etc
           Function: creats for you a sequence with its sheets, lables and helixes and prints them in tandem
        """

        # HELIX symbols(/) and its lables
        seq3D = []
        lable3D= []                                 # empty list for the lable line
        for i in range(0, len(seq)):
            seq3D.append("-")
            lable3D.append(" ")                     # append an empty space for our lables

        with open(load_file, 'r') as f:
            helixIndexes = []                      # new empty list for appending all indexes for the helix chain that will enable us to replace dashes with helix symbols
            lableIndexes = []                      # new empty list for appending index where each helix is located
            lables = []                            # empty list for the chain numbers
            for line in f:
                if line.startswith('HELIX'):
                    newl = line.split()[:]            # split our lines into a list with individual items that we can easily access
                    if newl[4] == chain:
                        frm = int(newl[5])          # Extract the start sequence index from the pdb
                        to = int(newl[8])           # Extract the end index for the helix from the pdb file
                        lables.append(newl[2])       # appends the lable for all the helixes on alist
                        lableIndexes.append(frm)     # append the indexes that will  mark  the point the helix is starting
                        for i in range(frm,to+1):      # using the range extracted above prints in to the list all the indexes of the aa in that helix to a list
                            helixIndexes.append(i)

        for i in range(0,len(lableIndexes)):         # convert the values on the LableIndex list into integers
            lableIndexes[i] = int(lableIndexes[i])

        for (index, lable) in zip(lableIndexes, lables): # Replacing the lable3D list at the specific indexes with the lables
            if len(lable) > 1:                                      # if the lable has more lab one character we want to make the two characters to be read as one
                lable3D[index-1:index+len(lable)-1] =lable
            else:
                lable3D[index-1] = lable
        labler = ("".join(lable3D))    

        replace = ''                                    # creating a string containg the symbols for helixes for each index for the index list created before(helixIndex)
        for i in range(0,len(helixIndexes)+1):
            replace+="/"

        for i in range(0,len(helixIndexes)):            # convertring items in the list in to integers
            helixIndexes[i] = int(helixIndexes[i])

        for (index, r) in zip(helixIndexes, replace):  # replacing the list of dashes(seq3D) which represents the sequence with helix symbols, where they are occuring
            seq3D[index-1] = r
        sequence3d= "".join(seq3D)


        # SHEEET | representation

        with open(load_file, 'r') as f:         # we use the three lists from the that heve undergone helix procesing i.e we append the sheet symbols and lables to them
            sheetIndex = []                     # we start and empty list for the sheet indexes
            lablesSheet = []                          # for appending lables for the sheet
            lableIndexesSheets = []                    # for appending indexes for labling
            for line in f:
                if line.startswith('SHEET'):
                    l = line.split()[1:]            # split our lines into a list with individual items that we can easily access
                    if l[4] == chain:
                        start = int(l[5])                            # Extract the start sequence index from the pdb
                        end = int(l[8])                              # Extract the end index for the sheet from the pdb file
                        lableIndexesSheets.append(start)             # append the indexes that will  mark  the point the sheet is starting
                        lablesSheet.append((str(l[0])+(str(l[1]))))  # appends the lable for all the helixes on alist

                        for i in range(start,end+1):                 # using the range extracted above prints in to the list all the indexes of the aa in that sheet to a list
                            sheetIndex.append(i)
            else:
                pass

        for i in range(0,len(lableIndexesSheets)):         # convert the values on the LableIndex list into integers
            lableIndexesSheets[i] = int(lableIndexesSheets[i])

        for (index, labl) in zip(lableIndexesSheets, lablesSheet): # Replacing the lable3D list at the specific indexes with the lables
            if len(labl) > 1:                                      # if the lable has more lab one character we want to make the two characters to be read as one
                lable3D[index-1:index+len(labl)-1] =labl
            else:
                lable3D[index-1] = labl                   
        lablerSheet = ("".join(lable3D))    

        sheetReplacer = []                                    # creating a string containg the symbols for sheet for each index for the index list created before(sheetIndex)
        for i in range(0, len(sheetIndex)+1):
            sheetReplacer.append("|")

        for i in range(0,len(sheetIndex)):            # convertring items in the list in to integers
            sheetIndex[i] = int(sheetIndex[i])

        for (index, r) in zip(sheetIndex, sheetReplacer):  # replacing the list of dashes(seq3D) which represents the sequence with helix symbols, where they are occuring
            seq3D[index-1] = r
        sequence3dSheet = "".join(seq3D)


        def print80char(seq, seqSymbols, seqLables):
            """Input: Amino acid string sequence, Amino acid string with symbols, Amino acid string of sequence lables
               Function: prints 80 characters of the three seqences in tandem        
            """
            print("Chain %s:\n(1)"%chain)
            for c in range(0,len(seq),80):
                print(seq[c:c+80]+"\n"+ seqSymbols[c:c+80]+"\n"+seqLables[c:c+80]+"\n")
                
        print80char(seq,sequence3dSheet,lablerSheet)
        print("(%d)"%len(seq),"\n")                     # print length of the sequence



    aa_dic = {'A':'ALA', 'R':'ARG', 'N':'ASN', 'D':'ASP', 'G':'GLY', 'Q':'GLN', 'E':'GLU', 'H':'HIS','C':'CYS',\
              'I':'ILE', 'L':'LEU', 'K':'LYS', 'M':'MET', 'F':'PHE', 'P':'PRO', 'S':'SER', 'T':'THR', 'W':'TRP', 'Y':'TYR', 'V':'VAL'} # dictionary for amino acids
    new_dict = dict([(value, key) for (key, value) in aa_dic.items()]) # swapped the values and keys 


    with open(load_file, 'r') as f:
        chains = []
        for line in f:
            if line.startswith('SEQRES'):
                l = line.split()[2:]         
                chains.append(l[0])                     # Appends all the chains found on the chain identifier column to an empty list
                chains = (list(dict.fromkeys(chains)))  # removes repeated chain names to remain with only individual chain names

        for i in chains:
            seq = ""
            with open(load_file, 'r') as f:
                for line in f:
                    l = line.split()
                    if line.startswith('SEQRES')and i == l[2]:
                        l = l[4:]
                        c = [new_dict[codon]for codon in l]
                        seq += "".join(c)
            seq_helix_sheet3D(load_file,seq,i)
        menu()

# CHOICE X - Export pdb
def choiceX():
    """Function: Exports your file to a pdb file"""
    exported = input("Enter the file path and name you want to export including the '.pdb' extension: ")
    with open(load_file) as f:
        with open(exported, "w+") as fx:
            for line in f:
                fx.write(line) 
    menu()



# Running the software
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
