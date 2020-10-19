def has_no_e(): #define function with no input attribute
    counter=0 #initiate a counter
    word=input('Please enter a word to test if it contains the letter "e":')
    if 'e' in word: #tests if letter 'e' appears in the string
        for index in word: #loops for each letter of the string
            if index == 'e': #if that letter is an 'e' it incremements the counter
                counter = counter+1
        print('Yes, the word',word,'contains the letter "e"',counter,'times')
    else:
        print('No, that word does not contain the letter "e".')


