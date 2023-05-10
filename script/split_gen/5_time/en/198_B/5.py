def isPalindrome(n):
    nlist = list(str(n))
    for i in range(len(nlist)//2):
        if nlist[i] != nlist[-i-1]:
            return False
    return True
