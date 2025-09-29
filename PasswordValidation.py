import os
import sys
import re
import ldapCheck
import time
from sys import argv

#import requests
from datetime import datetime
__author__     = "Max Hyppolite"
__version__    = "1.0.0"
__maintainer__ = "Max Hyppolite"
__email__      = "itsec-ops@harvard.edu"
__name__       = "Password_Validation"

'''
******************************************************************************************************************************************
* This script validates that the passwords meet the Harvard Complexity Standards                                                         *
*                                                                                                                                        *
* Input Files:                                                                                                                           *
*                  1) Password File (user provided csv file)                                                                                                      *
*                                                                                                                                        *
* Output files:                                                                                                                          *
*                  2) Passords that need to be run against LDAP (checkPassword.csv)                                                                          *
*                                                                                                                                        *
* Notes:     Check input file to see what delimiter character is being used. Mod the "delimiter" Variable in the Global Variables section *
*                                                                                                                                        *
******************************************************************************************************************************************

 Maintenace/Debbug/Additions: format: Date --> Who --> Description
 Example:
   06/09/2022 M.Hyppolite --> Creation Date
   06/14/2022 M.Hyppolite --> Added Outputfile
   08/02/2022 L.Smith     --> Added LDAP check module
   08/02/2022 L.Smith     --> Updated documenation
 '''

# Global Variables
today = datetime.now()
todayFormatted = today.strftime('%Y-%m-%d')
counter = 0

print('File Name: {0}'.format(sys.argv[1]))

def special_Val(value):

 if re.search("[@_!$%^&*()<>?/\|}{~:#]",value) == None:
       character_found=False

 else:
       character_found=True

 return character_found

def containsNumber(value):

    for character in value:
        if character.isdigit():
            return True
    return False

def passComplexity(value):
    counter = 0

    if re.search("[a-zA-Z]",value) != None:
        mixed_case = not value.islower() and not value.isupper()
        if mixed_case == True:
            counter +=1
            if containsNumber(value) == True:
                counter +=1
                if special_Val(value) == True:
                    counter +=1

    if counter >=2:
        Output.write('{0}:{1} \n'.format(userName,password))

def ldapVerification():
    validAccounts = open('validAccounts.csv', 'a')
    validAccounts.write("Username,Password,Valid_Password\n")

    with open('checkPassword.csv','r') as suspiciousCreds:
        for line in suspiciousCreds:
            delimiter=':'
            removeWhiteSpaces = line.strip()
            PasswordCheck = removeWhiteSpaces.split(delimiter)
            userName=PasswordCheck[0]
            password=PasswordCheck[1]

            validPassword = ldapCheck.main(userName,password)
            if validPassword == True:
                print("{0},{1},{2}".format(userName,password,validPassword))
                validAccounts.write("{0},{1},{2}\n".format(userName,password,validPassword))
            else:
                print("fail")
            time.sleep(1)


if __name__ == 'Password_Validation':
    Output = open('checkPassword.csv'.format(todayFormatted),'w')
    with open(sys.argv[-1],'r') as f:
        for line in f:
            delimiter=':'
            removeWhiteSpaces = line.strip()
            PasswordCheck = removeWhiteSpaces.split(delimiter)
            userName=PasswordCheck[0]
            password=PasswordCheck[1]

            if (len(password)>20):
                Output.write('{0}:{1}'.format(userName,password))
            else:
                if re.search("\d{5}",password) == None:
                    passComplexityTest = passComplexity(password)


    Output.close()
    ldapVerification()
