#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'link-python-project/PythonMiniProject/Notebooks'))
	print(os.getcwd())
except:
	pass

#%%
with open("link-python-project/PythonMiniProject/Data/3AYU.pdb", 'r') as myfile:
    
    out2= myfile.readlines()
    print(out2)
    print(len(out2))


#%%
out1= open("link-python-project/PythonMiniProject/Data/3AYU.pdb", 'r')
line= out1.readline()
print(line)


#%%
out1= open("link-python-project/PythonMiniProject/Data/3AYU.pdb", 'r')
line= out1.readline()
line= out1.readline()
line= out1.readline()
line= out1.readline()


print(line)
print(len(line))




#%%
for i in range(4):
    print(i)



with open ('../Data/humchrx.txt', 'r') as humchrx:
    tag = False
    for line in humchrx:
        if line.startswith('name'):#print(line)
            tag = True
        if line.startswith('-'):
            tag = False
        if line.startswith('_'):
            continue
        if tag:
            lineList = line.split()
            if len(lineList) > 0:
                print(lineList[0])  #%%


#%%
# opens the pdb file for reading
with open("../Data/3AYU.pdb", 'r') as mypdb:
    tag = False
    for line in mypdb:
        if line.startswith('HEADER'):
            tag = True
            if tag:
                print(line, end='\n')
                print('- Title','Description of the experiment represented in the entry.',sep="\t", end='\n')
        if line.startswith('TITLE'):
              tag = True
              if tag:
                print(line)
        if line.startswith('DBRIEF'):
             tag = True 
             if tag:
                print(line)
        if line.startswith('SEQRES'):
             tag = True
             if tag:
                print(line)
        if line.startswith('HELIX'):
            tag = True
            if tag:
                print(line)
        if line.startswith('SHEET'):
            tag = True
            if tag:
                print(line)

#%%
# with open("link-python-project/PythonMiniProject/Data/3AYU.pdb", 'r') as mypdb:
#     tag = False
#     for line in mypdb:
#         if line.startswith('HEADER'):
#             tag = True
#             continue
#         if line.startswith('TITLE'):
#               tag = True
#               continue
#         if line.startswith('DBRIEF'):
#              tag = True 
#              continue
#         if line.startswith('SEQRES'):
#              tag = True
#              continue            
#         if line.startswith('HELIX'):
#             tag = True
#             continue
#         if line.startswith('SHEET'):
#             tag = True
#             if tag:
#                 print(line)

#%%
pwd

#%%
