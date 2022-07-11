def translate_into_snake_hiss(text):
    """Translate human text into snake hiss.
    
    All vowels change to capital letter S.
    All consonants change to lower letter s.
    Specified characters without change.
    Ignore other characters.
    """

    hiss = ''
    for character in text:
        if character in ['S', 's', ' ', '.', ',', '?', '!', '-', ':']:
            hiss += character
        elif character.lower() in ['a', 'e', 'i', 'o','u', 'y']:
            hiss += 'S'
        else:
            hiss += 's'
    return hiss