def div_num(n):
    count=0
    while n%2==0:
        n=n//2
        count+=1
    return count

if __name__ == '__main__':
    div_num()