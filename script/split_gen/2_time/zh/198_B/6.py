def isPalindromic(num):
    numStr = str(num)
    length = len(numStr)
    if length == 1:
        return True
    else:
        for i in range(length//2):
            if numStr[i] != numStr[length-i-1]:
                return False
        return True
