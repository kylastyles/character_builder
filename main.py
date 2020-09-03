import random

'''
Run with `python main.py`
'''

# declare a maximum number of characters allowed 
# to prevent resource overload
MAX_VALUE = 20

class Character():
    ages = [
        'middle-aged',
        'old',
        'young'
    ]
    extras = [
        'alone',
        'blind',
        'celebrated',
        'deaf',
        'disgraced',
        'handicapped',
        'married',
        'mentally ill',
        'healthy',
        'poor',
        'rich',
        'sick',
        'strong',
        'weak'
    ]
    eye_colors = [
        'black',
        'blue',
        'brown',
        'green',
        'grey',
        'hazel',
        'violet'
    ]
    genders = [
        'female',
        'male',
        'other gender'
    ]
    hair_colors = [
        'black',
        'blonde',
        'dark brown',
        'grey',
        'light brown',
        'no', # bald
        'red',
        'white',
        'yellow'
    ]
    personalities = [
        'creative',
        'friendly',
        'generous',
        'gregarious',
        'manipulative',
        'mean',
        'selfish',
        'shy',
        'stubborn',
        'wise'
    ]
    professions = [
        'artist',
        'care-giver',
        'chef',
        'doctor',
        'engineer',
        'entrepreneur',
        'government worker',
        'lawyer',
        'musician',
        'pilot',
        'public servant',
        'religious leader',
        'retail employee',
        'sailor',
        'scientist',
        'soldier',
        'student',
        'teacher',
        'therapist'
    ]
    skin_colors = [
        'albino',
        'black',
        'dark brown',
        'light brown',
        'olive',
        'pale',
        'rosey',
        'tan'
    ]

    def __init__(self):
        self.age = random.choice(Character.ages)
        self.extra = random.choice(Character.extras)
        self.eye_color = random.choice(Character.eye_colors)
        self.gender = random.choice(Character.genders)
        self.hair_color = random.choice(Character.hair_colors)
        self.personality = random.choice(Character.personalities)
        self.profession = random.choice(Character.professions)
        self.skin_color = random.choice(Character.skin_colors)

        # Mostly all combinations are allowed, except for specific albino traits
        if self.skin_color == 'albino':
            self.eye_color = 'pink'
            self.hair_color = 'white'

    def __repr__(self):

        article = 'a'
        if self.age.startswith(('a', 'e', 'i', 'o', 'u')):
            article += 'n'

        if self.gender == 'female':
            pronoun = 'she is'
        elif self.gender == 'male':
            pronoun = 'he is'
        else:
            pronoun = 'they are'

        return f'{article.capitalize()} {self.age}, {self.gender} {self.profession} with {self.eye_color} eyes, {self.hair_color} hair, and {self.skin_color} skin. {pronoun.capitalize()} {self.personality} and also {self.extra}.' 


if __name__ == '__main__':

    # get valid user input for number of characters to build
    num_characters = None
    while not num_characters:
        user_input = input('Please enter number of characters to build: ')
        try:
            num_characters = int(user_input)
            if num_characters > MAX_VALUE:
                print(f'ERROR: Number must not exceed {MAX_VALUE}')
                num_characters = None
        except ValueError:
            print('ERROR: Whole numbers only, ex. 10')
            num_characters = None

    # build and display characters
    character_list = [Character() for n in range(num_characters)]
    for x, character in enumerate(character_list, 1):
        print(str(x)+'.', character)
    
