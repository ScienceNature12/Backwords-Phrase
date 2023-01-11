#Code practice
#backwords phrase generator

phrase = " "
count = 0

while phrase== phrase and count != 14:
    phrase = input("enter a phrase to print backwords: ")
    while count != 14:
        print (phrase[::-1])
        count= count + 1
        if count % 5 == 0:  #Help from stacksoverflow
            print (phrase)
           
      
    

    
