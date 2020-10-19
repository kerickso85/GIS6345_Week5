def nested_sum():
    list1=[1,2,3]
    list2=[4,5]
    list3=[6]
    list4=[7,8,9,10]
    lol= list1 + list2 + list3 + list4 #in this case lol means 'list of lists' not 'laugh out loud' :D
    #lol creates a new list composed of all four, without modifying the original four lists
    print(sum(lol)) #adds up all of the values of each of the lists, output is the grand total




