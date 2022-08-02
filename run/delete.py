import os
import pandas as pd

def deleteInFile(file):
    file_df = pd.read_excel(file)
    for i, row in file_df.iterrows():
        print(f"{i}. {row['Website']}")
    print("Which entry would you like to delete?")
    to_del = int(input().strip())

    try: 
        file_df = file_df.drop(file_df.index[to_del])
        
        sprdsheet = pd.ExcelWriter(file, engine='xlsxwriter')
        file_df.to_excel(sprdsheet, index=False)
        sprdsheet.save()

        print("Delete another? (Y/N)")
        yn = str(input().strip())
        if yn == 'Y':
            return deleteInFile(file)
        else:
            return

    except IndexError:
        print("You're raising an index error! Try again? (Y/N)")
        yn = str(input().strip())
        if yn == 'Y':
            os.system('clear')
            return deleteInFile(file)
        else:
            return

def deleteEntry():
    os.system('clear')
    print("Enter the file name:")
    file_name = str(input().strip())
    file_name = file_name + '.xlsx'
    os.system('clear')
    deleteInFile(file_name)
    return


