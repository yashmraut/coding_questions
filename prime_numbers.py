def prime(number): 
    if number <= 1:
        return("Not Prime")
    for i in range(2,int(number**0.5)):
        if number%i == 0:
            return("Not prime")
    else:
        return("Prime")
            
number = 2
print(prime(number))

# print(int(11**0.5))

# for i in range(2,3):
#     print(i)

# asked in V4C.ai 