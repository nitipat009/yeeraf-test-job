#Nitipat Boongate
def ThreeFive() :
    both = 0; #valid %
    # num 1-100
    for a in range(1,101) : 
        #------Condition------#
        if(a % 3==0) : #if the number is divisible by 3 then print "Three"
            print("Three",end="")
            both += 1
        
        if(a% 5==0) : # if the number is divisible by 5 then print "Five"
            print("Five",end="")
            both += 1
        
        if(both >= 1) : #clear valid % condition
            print()
            both = 0
            continue; # No more %
        #------Condition------#
        print(a)
ThreeFive()

