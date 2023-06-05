def search(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    elif n==4:
        return 4
    elif n==5:
        return 5
    elif n==6:
        return 6
    elif n==7:
        return 7
    elif n==8:
        return 8
    elif n==9:
        return 9
    else:
        for i in range(1,10):
            if n>=i*10**(len(str(i)))+i:
                continue
            else:
                return i*10**(len(str(i)))+search(n-i*10**(len(str(i))))
n=int(input())
print(search(n-1))
