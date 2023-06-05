def print_sequence(n,m):
    if n == 0:
        print()
    elif n == 1:
        for i in range(1,m+1):
            print(i)
    else:
        for i in range(n,m+1):
            print_sequence(n-1,i-1)
n,m = map(int,input().split())
print_sequence(n,m)
