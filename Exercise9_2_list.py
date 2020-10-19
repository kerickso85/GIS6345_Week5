def has_no_e():
    fin=open('words.txt') #this assumes that the words.txt file is in the same directory as the .py
    counter=0
    print('The following words from your list contain the letter "e" at least one time:') #lets the user know what's going on
    for line in fin: #loops to check each line of the .txt file
        word=line.strip() #temporarily assigns each word to a string variable
        if 'e' in word:
            print(word)
            counter = counter+1
    percentage = counter/113809*100 #calculates the percentage based on a fixed count of words in the words.txt file;
    #one extra step to count words would be necessary if the function was used on any other .txt file than the one tested here
    percentage = round(percentage,2) #rounds the float to two decimal places
    print('That means',percentage,'% of words in the list contain the letter "e".')
        




