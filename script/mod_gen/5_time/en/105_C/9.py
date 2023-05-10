def base_minus_2(n):
    if n==0:
        return 0
    else:
        s=''
        while n!=0:
            if n%2==0:
                s+='0'
                n=n//2
            else:
                s+='1'
                n=(n-1)//(-2)
        return s[::-1]
n=int(input())
print(base_minus_2(n))

if __name__ == '__main__':
    base_minus_2()