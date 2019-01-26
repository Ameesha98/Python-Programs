import random
#for comparing user input with generated input
def guess_num():
    print("NUMBER GUESS")
    #for generating random float number with 2 decimal
    gen_num=round(random.uniform(1,10000), 2)
    for i in range(1,10):
        #for taking user input
        user_num=input("Guess the number")
        #for first five turns
        if i<=5:
            if user_num==str(gen_num):
                print("Congrats!!! You Won")
                return
            else:
                print("Oops! Wrong Guess.. Try again")
        #for next turns
        else:
            if user_num==str(gen_num):
                print("Congrats!!! You Won")
                return
            else:
                try:
                    #for getting percentage
                    percent=((gen_num-float(user_num))*100)/gen_num
                    #for raising exception
                    if(i==6 and percent>10):
                        raise Exception("Your number is more than 10 percent away!! Better luck next time")
                    elif(i==7 and percent>5):
                        raise Exception("Your number is more than 5 percent away!! Better luck next time")
                    elif(i==8 and percent>1):
                        raise Exception("Your number is more than 1 percent away!! Better luck next time")
                    elif(i==9 and percent>0.5):
                        raise Exception("Your number is more than 0.5 percent away!! Better luck next time")
                    else:
                        print("Guessed num: ",user_num)
                        print("Generated num: ",gen_num)
                        return
                except Exception as e:
                    print(e)
                    print("Guessed num: ",user_num)
                    print("Generated num: ",gen_num)
                    print("Restarting the game...")
                    #calling the function again
                    guess_num()
guess_num()                        
                
    
    
    
#print(user_num+" "+str(gen_num))
