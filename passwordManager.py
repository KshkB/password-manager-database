import os, sys

from run.options import programOptions
from run.createNew import createNew
from run.updaterecords import updateRecords
from run.searchfind import searchFind
from run.delete import deleteEntry

def manager():
    programOptions()
    print('Choose an option!')
    ans = int(input().strip())
    os.system('clear')

    if ans == 1:
        createNew()
        os.system('clear')
        return manager()
    
    if ans == 2:
        updateRecords()
        os.system('clear')
        return manager()
    
    if ans == 3:
        searchFind()
        os.system('clear')
        return manager()
    
    if ans == 4:
        deleteEntry()
        os.system('clear')
        return manager()
    
    if ans == 5:
        os.system('clear')
        sys.exit(0)
    
if __name__ == '__main__':
    os.system('clear')
    manager()

