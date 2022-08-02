import pandas as pd
import sys

def createNew():
    print('Enter the file name:')
    file_name = str(input().strip())
    file_name = file_name + '.xlsx'

    pw_cols = [ 
        'Website',
        'Username',
        'Password',
        'Further hints'
    ]

    dataframe = pd.DataFrame(columns = pw_cols)
    sprdsheet = pd.ExcelWriter(file_name, engine='xlsxwriter')
    dataframe.to_excel(sprdsheet, index=False)

    sprdsheet.save()

    print('Keep going? (Y/N)')
    ans = str(input().strip())
    if ans == 'Y':
        return
    else:
        sys.exit(0)

