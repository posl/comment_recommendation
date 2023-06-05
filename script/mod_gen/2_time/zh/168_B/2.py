def pronun(n):
    if n%10==2 or n%10==4 or n%10==5 or n%10==7 or n%10==9:
        return 'hon'
    elif n%10==0 or n%10==1 or n%10==6 or n%10==8:
        return 'pon'
    elif n%10==3:
        return 'bon'
n=int(input())
print(pronun(n))
