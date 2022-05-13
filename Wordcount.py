def Countword():
   filename = input("Enter The Path Of Your File: ")
   NumberOfWords = 0
   file = open(filename,"r")    
   for line in file:
       words=line.split()
       NumberOfWords = NumberOfWords+len(words)
   print("Number Of Words: ")
   print(NumberOfWords)

Countword() 



