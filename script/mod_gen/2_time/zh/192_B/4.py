def isHardToRead(s):
    #print('s=', s)
    odd = s[::2]
    even = s[1::2]
    #print('odd=', odd)
    #print('even=', even)
    if odd.islower() and even.isupper():
        return True
    else:
        return False

if __name__ == '__main__':
    isHardToRead()