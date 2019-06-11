#%% [markdown]
# ### Display menu

#%%
star_list=""
for i in range(5):
    star_list += '*'
    print(star_list)

    

# PDB FILE ANALYZER
# Select an option from below:
# 1)  Open a PDB file                      (O)
# 2)  Information                          (I)
# 3)  Show histrogram of amino acids       (H)
# 4)  Display Secondary Structure          (S)
# 5)  Export PDB File                      (X)
# 6)  Exit                                 (Q)
# Current PDB:None
#%%
software = "PDB FILE ANALYZER"
choices = "Select an option from below:"
c1 = "1) Open a PDB file                     (O)"
c2 = "2) Information                         (I)"
c3 = "3) Show histrogram of amino acids      (H)"
c4 = "4) Display Secondary Structure         (S)"
c5 = "5) Export PDB File                     (X)"
c6 = "6) Exit                                (Q)"
file = "None"
status = "Current PDB: "+ file
len(software)

stars="*"
space=" "
print(stars*80)
#The length of the inserted string and its 0 index is subtracted for the desired 80 characters per line to be met.
#Subtract index 0s in each object added, this concept is applied to each line.
print(stars * 1,"%0s"%"","%s" %software,space*(75-(len(software)))+stars )  
print(stars*80)
print(stars * 1,"%0s"%"","%s" %choices,space*(75-(len(choices)))+stars ) 
print(stars*1, space*76, stars*1)
print(stars * 1,"%5s"%"","%s" %c1,space*(70-(len(c1)))+stars )
print(stars * 1,"%5s"%"","%s"%c2,space*(70-(len(c2)))+stars )
print(stars * 1,"%5s"%"","%s" %c3,space*(70-(len(c3)))+stars )
print(stars * 1,"%5s"%"","%s" %c4,space*(70-(len(c4)))+stars )
print(stars * 1,"%5s"%"","%s" %c5,space*(70-(len(c5)))+stars )
print(stars * 1,"%5s"%"","%s" %c6,space*(70-(len(c6)))+stars )
print(stars * 1,"%0s"%"",space*(74-(len(status))),"%s" %status,stars*1)
print(stars*80)
# print(input(":"))










#%%
# My amino acid dictionary
aa_dic = {'A':'ALA', 'R':'ARG', 'N':'ASN', 'D':'ASP', 'C':'GLY', 'Q':'GLN', 'E':'GLU', 'H':'HIS', 'I':'ILE', 'L':'LEU', 'K':'LYS', 'M':'MET', 'F':'PHE', 'P':'PRO', 'S':'SER', 'T':'THR', 'W':'TRP', 'Y':'TYR', 'V':'VAL'}
type(aa_dic)
aa_dic

#%%
pwd
#%%
