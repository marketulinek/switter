def translate_into_snake_hiss(text):
    """Translate human text into snake hiss.
    
    Specified characters without change.
    All vowels change to capital letter S.
    Rest of characters change to lower letter s.
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