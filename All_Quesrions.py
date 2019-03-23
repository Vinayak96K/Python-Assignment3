#Helper function to initialize list
def InitList(larr=list()):
    ilen=int(input('Enter number of elements:'))
    for i in range(0,ilen):
        num=int(input('Enter num {} :'.format(i+1)))
        larr.append(num)
    print("Current list [larr]:{}".format(larr))
    return
    
#Helper function wich gets question number as an input and returns the desired output on list
def getResultOfQues(QNo):
    iRet=0
    itemp=0
    #init return variable
    if(QNo==2 or QNo==3):
        iRet=arr[0]
    elif(QNo==4):
        itemp=int(input("Enter number:"))
        iRet=0
    #iterate
    for i in range(0,len(arr)):
        #check question number
        if(QNo==1):
            iRet+=arr[i]
        elif(QNo==2):
            if(iRet<arr[i]):
                iRet=arr[i]
        elif(QNo==3):
            if(iRet>arr[i]):
                iRet=arr[i]
        elif(QNo==4):
            if(itemp==int(arr[i])):
                iRet+=1
        elif(QNo==5):
            if(chkPrime(int(arr[i]))==True):
                print(arr[i])
                iRet+=arr[i]    
        else:
            print('Incorrect input!')
            break            
    return iRet

#helper function to check prime number.
def chkPrime(no):
    i=int((no/2))+1
    while(i>1):
        if(no%i==0):
            break
        i-=1

    if(i==1):
        return True
    else:
        return False

#Create List
arr=list()
#Accept elements in list
InitList(arr)
print("Current list [arr]:{}".format(arr))

##----##----##----##----##----<< Question 1 >>----##----##----##----##----##
print('Addition is:{}'.format(int(getResultOfQues(1))))

##----##----##----##----##----<< Question 2 >>----##----##----##----##----##
print('Maximum is:{}'.format(int(getResultOfQues(2))))

##----##----##----##----##----<< Question 3 >>----##----##----##----##----##
print('Minimum is:{}'.format(int(getResultOfQues(3))))

##----##----##----##----##----<< Question 4 >>----##----##----##----##----##
print('Frequency is:{}'.format(int(getResultOfQues(4))))

##----##----##----##----##----<< Question 5 >>----##----##----##----##----##
print('Prime Addition is:{}'.format(int(getResultOfQues(5))))