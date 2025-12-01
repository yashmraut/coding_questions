def isPalindrome(x: int):

    if x < 0:
        return False
      
    number = 0
    temp_x = x
    remainder = 0

    while temp_x != 0:
        remainder = temp_x % 10
        temp_x = temp_x // 10
        number = number * 10 + remainder
    if x == number:
        return True
    else:
        return False

print(isPalindrome(121121))