import pandas as pd
import os, sys

def addNewSpecs(file):
    os.system('clear')
    print("Enter the website name:")
    website = str(input().strip())

    print("Enter your username:")
    usernm = str(input().strip())

    print("Enter your password:")
    pw = str(input().strip())

    print("Enter any further keywords as hints (if any)")
    hints = str(input().strip())

    file_df = pd.read_excel(file)
    file_df = file_df.append(
        pd.Series(
            [
                website, usernm, pw, hints
            ], index = file_df.columns
        ), ignore_index = True
    )

    sprdsheet = pd.ExcelWriter(file, engine='xlsxwriter')
    file_df.to_excel(sprdsheet, index = False)
    sprdsheet.save()

    os.system('clear')
    print("Add another website spec? (Y/N)")
    YorN = str(input().strip())
    if YorN == 'Y':
        return addNewSpecs(file)
    return

def updatePassword(file):

    file_dataframe = pd.read_excel(file)
    l = len(file_dataframe)
    print('Which website password do you wish to update?')
    print('1. Enter website name\n2. Choose from a list of all logged websites')
    ans = int(input().strip())

    if ans == 1:
        os.system('clear')
        print('Enter the website name:')
        web = str(input().strip())
        web = web.lower()

        possibilities = []
        for i, site in file_dataframe.iterrows():
            lowered = site['Website'].lower().replace(' ', '')
            if web in lowered:
                possibilities.append([i, site['Website']])

        if len(possibilities) == 0:
            print('Not found. Try again? (Y/N)')
            notfoundans = str(input().strip())
            if notfoundans == 'Y':
                return updatePassword(file)
            return 

        if len(possibilities) == 1:
            os.system('clear')
            print(f"Do you want to update the password for {possibilities[0][-1]}? (Y/N)")
            updans = str(input().strip())
            if updans == 'Y':
                ind = possibilities[0][0]
                print('Enter the new password:')
                newPass = str(input().strip())
                file_dataframe.at[ind, 'Password'] = newPass
                
                sprdsheet = pd.ExcelWriter(file, engine='xlsxwriter')
                file_dataframe.to_excel(sprdsheet, index=False)
                sprdsheet.save()

                os.system('clear')
                print('Update another website password? (Y/N)')
                updans = str(input().strip())
                if updans == 'Y':
                    return updatePassword(file)
                else:
                    return 

            print('Update another? (Y/N)')
            ans2 = str(input().strip())
            if ans2 == 'Y':
                os.system('clear')
                return updatePassword(file)
            return 

        os.system('clear') 
        print('Choose which website to update:')
        for i, v in enumerate(possibilities):
            print(f"{i}. {v[-1]}")
            
        updt_optn = int(input().strip())
            
        os.system('clear')
        print('Enter the new password:')
        newPass = str(input().strip())

        ind = possibilities[updt_optn][0]
        file_dataframe.at[ind, 'Password'] = newPass
            
        sprdsheet = pd.ExcelWriter(file, engine='xlsxwriter')
        file_dataframe.to_excel(sprdsheet, index=False)
        sprdsheet.save()

        os.system('clear')
        print('Update another website password? (Y/N)')
        updans = str(input().strip())
        if updans == 'Y':
            return updatePassword(file)
        else:
            return 

    if ans == 2:
        os.system('clear')
        print('Choose one:')
        for i, row in file_dataframe.iterrows():
            print(f"{i}. {row['Website']}")

        choice = int(input().strip())

        os.system('clear')
        print('Enter the new password:')
        newPass = str(input().strip())

        file_dataframe.at[choice, 'Password'] = newPass
        
        sprdsheet = pd.ExcelWriter(file, engine='xlsxwriter')
        file_dataframe.to_excel(sprdsheet, index=False)
        sprdsheet.save()

        os.system('clear')
        print('Update another website password? (Y/N)')
        updans = str(input().strip())
        if updans == 'Y':
            os.system('clear')
            return updatePassword(file)
        else:
            os.system('clear')
            return 

def updateRecords():
    print('Enter the name of the file to update:')
    file_name = str(input().strip())
    file_name = file_name + '.xlsx'
    if bool(os.path.isfile(file_name)):
        os.system('clear')
        print('Cool, it is here!')

        print('Choose:\n1. Add new website specs\n2. Update password\n3. Return to main')
        ans = int(input().strip())

        if ans == 1:
            os.system('clear')
            return addNewSpecs(file_name)

        if ans==2:
            os.system('clear')
            return updatePassword(file_name)

        if ans == 3:
            return 

    else:
        print("Not here mate. Try again? (Y/N)")
        nothere = str(input().strip())
        if nothere == 'Y':
            return
        else:
            os.system('clear')
            sys.exit(0)

