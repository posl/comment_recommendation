def count(n):
    count=0
    for i in range(1,n+1):
        if not '7' in str(i) and not '7' in oct(i):
            count+=1
    return count
print(count(100000))
