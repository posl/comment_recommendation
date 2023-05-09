def century(n):
    #divmod returns quotient and remainder
    q,r = divmod(n,100)
    if r == 0:
        return q
    else:
        return q+1
n = int(input())
print(century(n))

if __name__ == '__main__':
    century()