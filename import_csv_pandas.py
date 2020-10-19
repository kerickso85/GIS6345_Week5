import matplotlib
import pandas
path='test_data.csv' #my test data with 29,205 indexed records with ten columns/eachtable1=pandas.read_csv(path)
#print(type(table1)) #debug to make sure I actually imported CSV as a Data Frame
print(table1.head(7)) #display the first seven records of table
table2=pandas.DataFrame(table1, columns=['Sigma0_HH_Stack'])
#print(type(table2)) #debug to make sure I actually created a subset Data Frame
print(table2.head(15)) #display the first fifteen records of subset
table2.plot() #produce a graph of Sigma0 for HH polarized values over the range of pixels
