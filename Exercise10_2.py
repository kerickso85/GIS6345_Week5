def cumsum():
    #create a list containing all prime numbers up to 100
    my_primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    index=0
    cumulative=0
    cumulative_list=[] #define index, cumulative sum variable, and new cumulative list
    for value in my_primes:
        cumulative=cumulative+my_primes[index] #add current value to previous cumulative amount
        if index<len(my_primes):
            #print('Current list index',index) #debug statement
            #print('Current list value',my_primes[index]) #debug statement
            #print('Current cumulative sum:',cumulative) #debug statement
            cumulative_list.append(cumulative)
            #print('Growing list of cumulative sum of primes:',cumulative_list) #debug statement
            index=index+1 #increment which value in the list is being considered
    print('The list of prime numbers less than 100 is:',my_primes)
    print('The sum of primes numbers less than 100 is:',cumulative)
    print('The new, cumulative sum list is:',cumulative_list)





