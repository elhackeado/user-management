# This file contains the data validation functions

# NOTE: Currently only empty value validations is implemented, further validations must be implemented to make sure that application data remains consistent

# check if string is empty or null
def notEmptyString(str):
    if str==None:
        return False
    if  len(str.strip())==0:
        return False
    return True