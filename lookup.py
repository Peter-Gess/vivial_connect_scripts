# Script to demonstrate buying a number via the CLI

from vivialconnect import Resource, Number

# Configure SDK
Resource.api_key = ""
Resource.api_secret = ""
Resource.api_account_id = ""

def find_number():
    numbers = Number.available(country_code='US',
                           number_type='local',
                           area_code='651',
                           in_postal_code=None,
                           in_region=None,
                           limit=5)
    for number in numbers:
        print(number.name, number.phone_number_type, number.phone_number)


def buy_number(phone_number=None, phone_number_type='local'):
    
    number = Number()
    number.phone_number = phone_number
    number.phone_number_type = phone_number_type
    number.buy()
    print('You bought {}'.format(phone_number))


def list_numbers():
    numbers = Number.find()
    for number in numbers:
        print(number.id, number.name, number.phone_number_type, number.phone_number)


def release_number(id=None, phone_number=None):
    number = Number()
    numbers = Number.find()
    for number in numbers:
        if number == id:
            number.destroy()
            print('{} has been removed from your account'.format(number.phone_number))
    if id not in numbers:
        print("not a valid id")

