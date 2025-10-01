import sys
import re
import ldapCheck
import time
from datetime import datetime

__author__ = "Max Hyppolite"
__version__ = "1.0.0"
__maintainer__ = "Max Hyppolite"
__email__ = "itsec-ops@harvard.edu"

# *********************************************************************
# * This script validates that the passwords meet the Harvard Complexity Standards *
# *
# * Input Files: *
# *     1) Password File (user provided csv file) *
# *
# * Output files: *
# *     2) Passwords that need to be run against LDAP (checkPassword.csv) *
# *
# * Notes: Check input file to see what delimiter character is being used. *
# *        Modify the "delimiter" Variable in the Global Variables section. *
# *
# *********************************************************************
# Maintenance/Debug/Additions: format: Date --> Who --> Description
# Example:
#   06/09/2022 M.Hyppolite --> Creation Date
#   06/14/2022 M.Hyppolite --> Added Outputfile
#   08/02/2022 L.Smith     --> Added LDAP check module
#   08/02/2022 L.Smith     --> Updated documentation

# Global Variables
today = datetime.now()
today_formatted = today.strftime('%Y-%m-%d')
counter = 0

print('File Name: {0}'.format(sys.argv[1]))


def special_val(value):
    # Returns True if any special character is found in value, else False
    if re.search(r"[@_!$%^&*()<>?/\|}{~:#]", value) is None:
        character_found = False
    else:
        character_found = True
    return character_found


def contains_number(value):
    for character in value:
        if character.isdigit():
            return True
    return False


def pass_complexity(value):
    counter = 0

    if re.search(r"[a-zA-Z]", value) is not None:
        mixed_case = not value.islower() and not value.isupper()
        if mixed_case:
            counter += 1
            if contains_number(value):
                counter += 1
                if special_val(value):
                    counter += 1

    if counter >= 2:
        Output.write('{0}:{1}\n'.format(userName, password))


def ldap_verification():
    valid_accounts = open('validAccounts.csv', 'a')
    valid_accounts.write("Username,Password,Valid_Password\n")

    with open('checkPassword.csv', 'r') as suspicious_creds:
        for line in suspicious_creds:
            delimiter = ':'
            remove_whitespaces = line.strip()
            password_check = remove_whitespaces.split(delimiter)
            userName = password_check[0]
            password = password_check[1]

            valid_password = ldapCheck.main(userName, password)
            if valid_password:
                print("{0},{1},{2}".format(userName, password, valid_password))
                valid_accounts.write(
                    "{0},{1},{2}\n".format(userName, password, valid_password)
                )
            else:
                print("fail")
            time.sleep(1)
    valid_accounts.close()


if __name__ == '__main__':
    Output = open('checkPassword.csv', 'w')
    with open(sys.argv[-1], 'r') as f:
        for line in f:
            delimiter = ':'
            remove_whitespaces = line.strip()
            password_check = remove_whitespaces.split(delimiter)
            userName = password_check[0]
            password = password_check[1]

            if len(password) > 20:
                Output.write('{0}:{1}\n'.format(userName, password))
            else:
                if re.search(r"\d{5}", password) is None:
                    pass_complexity_test = pass_complexity(password)
    Output.close()
    ldap_verification()
