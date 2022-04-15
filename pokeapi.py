import requests

def pokemon1(pokename):
    """
    get's a bunch of info from the pokeapi
    :param pokename:
    :return: dictionary full of pokemon info
    """
    print("Getting pokemon info...")

    url = 'https://pokeapi.co/api/v2/pokemon/' + pokename  # puts pokemon name into the url
    r = requests.get(url)  # storing request into r variable

    if r.status_code == 200:
        print('Successful!')
        return r.json()
    else:
        print("Failed to obtain pokemon info, Code: " + str(r.status_code))
        return