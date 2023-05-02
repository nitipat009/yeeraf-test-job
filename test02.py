#Nitipat Boongate
x = input("Input: ")
try: # Valid Input Form
    #Seperate Input
    nums = list(map(int,x.split("=")[1].split('[')[1].split(']')[0].split(",")))
    sumInput = int(x.split("=")[-1])
    #Validate
    checked = 0;
    for outside in range(len(nums)-1) :
        if(checked == 1) : # found Break
            break;
        for inside in range(outside+1,len(nums)) :
            if(nums[outside] + nums[inside] == sumInput):
                print('Output: {0},{1}'.format(outside,inside))
                print('Explanation: Because nums[{0}] + nums[{1}] = {2}'.format(outside,inside,sumInput))
                checked = 1
                break;
    if(checked == 0) :
        print('Output: no output')
        print('Explanation: The are no two numbers that add up to {0}'.format(sumInput))
except :
    print('Input Form Error!')


            
