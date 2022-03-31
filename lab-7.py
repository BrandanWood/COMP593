# Script made by Brandan Wood Comp 593 - Section 02
# description: Making a complex data structure and then utilizing it with functions.
# Use: python lab-7.py

def main():
    # dicionary made containing information
    aboutMe = {
        'name': "Brandan Wood",
        'studentID': 10268250,
        'favoriteToppings': ["Pepperoni",
                            "Green Peppers",
                            "Mushrooms"],
        'movies': [
            {'movieTitle': 'Kung Fu Panda',
             'genre': 'Wuxia'
             },
            {'movieTitle': 'John Wick',
             'genre': 'Action'
             },
        ]
    }

    # adding a new movie
    newMovie = {'movieTitle': 'Shrek', 'genre': 'Fantasy'}
    aboutMe['movies'].append(newMovie)

    # adding more toppings
    newToppings = ('Pineapple', 'Ham')
    addToppings(aboutMe, newToppings)

    # Sentence Printing
    printAboutMe(aboutMe)

# function that appends new toppings and sorts them.
def addToppings(aboutMe, newToppings):
    toppingList = aboutMe['favoriteToppings']
    for t in newToppings:
        toppingList.append(t)
        toppingList.sort()

def printAboutMe(aboutMe):
    print('Hi Jeremy, my name is ' + aboutMe['name'] + ', and my student ID is ' + str(aboutMe['studentID']))
    num = 0
    num2 = 0
    toppingSentence = "My ideal pizza has "
    for _ in aboutMe['favoriteToppings']:
        toppingSentence += aboutMe['favoriteToppings'][num]
        num += 1
        if num < len(aboutMe['favoriteToppings']) - 1:
            toppingSentence += ', '
        elif num == len(aboutMe['favoriteToppings']) - 1:
            toppingSentence += ' and '
        else:
            toppingSentence += '.'

    genreSentence = "I like to watch "
    movieSentence = "Some of my favourites are "
    for i in aboutMe['movies']:
        genreSentence += aboutMe['movies'][num2]['genre']
        movieSentence += aboutMe['movies'][num2]['movieTitle']
        num2 += 1
        if num2 < len(aboutMe['movies']) - 1:
            genreSentence += ', '
            movieSentence += ', '
        elif num2 == len(aboutMe['movies']) - 1:
            genreSentence += ' and '
            movieSentence += ' and '
        else:
            genreSentence += ' movies.'
            movieSentence += '!'


    print(toppingSentence)
    print(genreSentence)
    print(movieSentence)

main()






