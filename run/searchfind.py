import os, sys
import pandas as pd

def searchInFile(file):

    file_dataframe = pd.read_excel(file)
    l = len(file_dataframe)

    print('Search by:\n1. Website name\n2. Username')
    searchby = int(input().strip())
    
    if searchby == 1:
        print("Enter the name of the website:")
        webname = str(input().strip())
        webname = webname.lower().replace(' ', '')


        possible_websites = []
        for ind, row in file_dataframe.iterrows():
            lowered = row['Website'].lower().replace(' ', '')
            if webname in lowered:
                possible_websites.append([ind, row['Website']])

        if len(possible_websites) == 0:
            print("Not found. Try again? (Y/N)")
            ans = str(input().strip())
            if ans == 'Y':
                return searchInFile(file)
            return

        if len(possible_websites) == 1:
            os.system('clear')
            print("Found 'em!")
            ind = possible_websites[0][0]
            print(f"\n{file_dataframe.loc[[ind]].to_string(index=False)}\n")

        if len(possible_websites) > 1:
            os.system('clear')
            print(f"Here are all the listed websites containing {webname}.\nWhich website entry would you like to see?")
            for item in possible_websites:
                print(f"{item[0]}. {item[-1]}")

            ans = int(input().strip())
            os.system('clear')
            print(file_dataframe.loc[[ans]].to_string(index=False))

        return

    if searchby == 2:
        os.system('clear')
        print("Enter username:")
        usernm = str(input().strip())
        users = [file_dataframe.loc[i, 'Username'] for i in range(l)]

        sortByInput = []
        for i, nm in enumerate(users):
            nm_lowered = nm.lower()
            if usernm in nm_lowered:
                sortByInput.append([i, nm])

        if len(sortByInput) > 0:
            cols = [ 
                'Website', 'Username', 'Password', 'Further hints'
            ]
            new_df = pd.DataFrame(columns = cols)
            os.system('clear')
            print(f"Here are all the websites with username containing {usernm}:\n")
            for item in sortByInput:
                ind = item[0]
                new_df = new_df.append(
                        file_dataframe.loc[ind]
                )
#                print(file_dataframe.loc[index])
            print(new_df.to_string(index=False))

            print(f"\nSearch again? (Y/N)")
            yorn = str(input().strip())
            if yorn == 'Y':
                return searchInFile(file)
            return

        else:
            print(f"\nNo usernames found containing {usernm}, try again? (Y/N)")
            yorn = str(input().strip())
            if yorn == 'Y':
                return searchInFile(file)
            return      

def searchFind():
    os.system('clear')
    print('Enter the name of the file you want to search:')
    file_name = str(input().strip())
    file_name = file_name + '.xlsx'
    if bool(os.path.isfile(file_name)):
        os.system('clear')
        print('Cool, it is here!')
        data = pd.read_excel(file_name)

        print("Would you like to:\n1. List all entries\n2. Search and return a particular\n3. Back to main")
        searchfindans = int(input().strip())
        if searchfindans == 1:
            os.system('clear')
            print(data.to_string(index=False))
            print('\nBack to main or are we done here?\n1. Back to main\n2. Back to search menu')
            ans = int(input().strip())
            if ans == 1:
                return
            if ans == 2:
                os.system('clear')
                return searchFind()

        if searchfindans == 2:
            os.system('clear')
            searchInFile(file_name)

            print("\nWhat are we doing now, my fine feathered friend?\n1. Back to main\n2. Search again")
            ans = int(input().strip())
            if ans == 1:
                return 
            if ans == 2:
                os.system('clear')
                return searchInFile(file_name)

        if searchfindans == 3:
            return

    else:
        print("Not here mate. Try again? (Y/N)")
        nothere = str(input().strip())
        if nothere == 'Y':
            return
        else:
            sys.exit(0)

