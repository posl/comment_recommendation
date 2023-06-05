def next_abc(n):
    if n%111==0:
        return n
    else:
        return (n//111+1)*111
n=int(input())
print(next_abc(n))
