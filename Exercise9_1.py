fin=open('words.txt') #this assumes that the words.txt file is in the same directory as the .py
for line in fin: #loop to check each line of the list
    word=line.strip() #temporarily assign each word to a string variable
    if len(word)>20: #test if the length of the word is greater than 20 chars
        print(word) #if so, print out





