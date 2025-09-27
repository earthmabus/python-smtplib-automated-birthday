import email_account
from birthday_list import BirthdayList
import random
import datetime as dt

BIRTHDAY_LETTERS = [ "./inputs/bday_letter1.txt" , "./inputs/bday_letter2.txt", "./inputs/bday_letter3.txt" ]
EMAIL_ADDRESS = "earthmabus@gmail.com"
EMAIL_PASSWORD_FILE = "./password.txt"
CURRENT_DATE_YEAR = dt.datetime.now().year
CURRENT_DATE_MONTH = dt.datetime.now().month
CURRENT_DATE_DAY = dt.datetime.now().day

def load_password():
    '''loads the password for the email account from PASSWORD_FILE'''
    retval = ""
    with open(EMAIL_PASSWORD_FILE, "r") as file_password:
        retval = file_password.readline().strip()
    return retval

def craft_birthday_letter(name):
    '''creates a list of string representing the birthday message'''
    # select a random birthday letter
    bday_letter = random.choice(BIRTHDAY_LETTERS)
    with open(bday_letter, "r") as file_bday_letter:
        lines = file_bday_letter.readlines()

    # replace [name] with the name of person
    updated_lines = [l.replace("[name]", name) for l in lines]

    return updated_lines

# load the list of birthdays
bday_list = BirthdayList()
bday_list.load()

# get the list of birthdays for a specified day
print(f"Today is {CURRENT_DATE_MONTH}/{CURRENT_DATE_DAY}/{CURRENT_DATE_YEAR}")
birthday_people = bday_list.get_birthdays_for_date(CURRENT_DATE_MONTH, CURRENT_DATE_DAY)
print(f"There are {len(birthday_people)} birthdays for month={CURRENT_DATE_MONTH}, day={CURRENT_DATE_DAY}")

# for each birthday person, send a random birthday email
for p in birthday_people:
    bday_name = p['name'].strip()
    bday_email = p['email'].strip()

    # construct a birthday letter for the person
    lines = craft_birthday_letter(bday_name)
    bday_letter = ""
    for l in lines:
        bday_letter = bday_letter + l

    # email the letter out
    password = load_password()
    account = email_account.EmailAccount(EMAIL_ADDRESS, password)
    account.send_email(bday_email, f"Happy birthday, {bday_name}!", bday_letter)
    print(f"Successfully sent birthday email to {bday_name}!")
