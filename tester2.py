def myMovieLife(lastname_fstletter, birth_month, cell_digit):
    suffix = "month"
    months_val = months(cell_digit)
    if months_val > 1 :
        suffix = "months"
    return "The " + \
           str(status(cell_digit)) + " " + \
           adjective(lastname_fstletter) + " " + \
           subject(birth_month) + " " + \
           complement(cell_digit) + " " + \
           "in " + \
           str(months_val) + " " + \
           suffix


def status(cell_digit):
    if cell_digit % 2 == 0:
        return True
    else:
        return False


def adjective(lastname_fstletter):
    if lastname_fstletter == 'A':
        return 'awesome'
    elif lastname_fstletter == 'B':
        return 'shocking'
    elif lastname_fstletter == 'C':
        return 'hilarious'
    elif lastname_fstletter == 'D':
        return 'fascinating'
    elif lastname_fstletter == 'E':
        return 'marvelous'
    elif lastname_fstletter == 'F':
        return 'unbelievable'
    elif lastname_fstletter == 'G':
        return 'funny'
    elif lastname_fstletter == 'H':
        return 'epic'
    elif lastname_fstletter == 'I':
        return 'thrilling'
    elif lastname_fstletter == 'J':
        return 'wonderful'
    elif lastname_fstletter == 'K':
        return 'dramatic'
    elif lastname_fstletter == 'L':
        return 'intriguing'
    elif lastname_fstletter == 'M':
        return 'courageous'
    elif lastname_fstletter == 'N':
        return 'beautiful'
    elif lastname_fstletter == 'O':
        return 'bracing'
    elif lastname_fstletter == 'P':
        return 'lively'
    elif lastname_fstletter == 'Q':
        return 'dangerous'
    elif lastname_fstletter == 'R':
        return 'impressive'
    elif lastname_fstletter == 'S':
        return 'astonishing'
    elif lastname_fstletter == 'T':
        return 'interesting'
    elif lastname_fstletter == 'U':
        return 'unexpected'
    elif lastname_fstletter == 'V':
        return 'surprising'
    elif lastname_fstletter == 'W':
        return 'lovely'
    elif lastname_fstletter == 'X':
        return 'electrifying'
    elif lastname_fstletter == 'Y':
        return 'commoving'
    elif lastname_fstletter == 'Z':
        return 'overwhelming'


def subject(birth_month):
    if birth_month == "Jan":
        return "biography"
    if birth_month == "Feb":
        return "history"
    if birth_month == "Mar":
        return "legend"
    if birth_month == "Apr":
        return "life"
    if birth_month == "May":
        return "anecdote"
    if birth_month == "Jun":
        return "revenge"
    if birth_month == "Jul":
        return "mission"
    if birth_month == "Aug":
        return "existence"
    if birth_month == "Sep":
        return "battle"
    if birth_month == "Oct":
        return "chronicle"
    if birth_month == "Nov":
        return "combat"
    if birth_month == "Dec":
        return "fairy tale"


def complement(cell_digit):
    if cell_digit == 0:
        return "of an adventurer"
    if cell_digit == 1:
        return "of a warrior"
    if cell_digit == 2:
        return "of a genius"
    if cell_digit == 3:
        return "of a movie star"
    if cell_digit == 4:
        return "of a hero"
    if cell_digit == 5:
        return "of a scientific"
    if cell_digit == 6:
        return "of a dreamer"
    if cell_digit == 7:
        return "of a cowboy"
    if cell_digit == 8:
        return "of a jedi"
    if cell_digit == 9:
        return "of an ogre"


def months(cell_digit):
    days = (cell_digit ** ((cell_digit % 2) + 1)) * cell_digit
    if cell_digit == 0:
        return 1
    if days % 30 == 0:
        return days // 30
    else:
        return (days // 30) + 1

print(months(9))