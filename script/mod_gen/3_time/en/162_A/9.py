def is_seven(n):
    #convert n to a string
    s = str(n)
    #check if 7 is in the string
    if '7' in s:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    is_seven()