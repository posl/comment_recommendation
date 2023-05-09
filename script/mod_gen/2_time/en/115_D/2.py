def burger(n,x):
    if n == 0:
        return 1 if x > 0 else 0
    elif x == 1:
        return 0
    elif x <= 1 + burger(n-1,0):
        return burger(n-1,x-1)
    elif x == 2 + burger(n-1,0):
        return 1 + burger(n-1,0)
    elif x <= 2 + 2*burger(n-1,0):
        return 1 + burger(n-1,x-2-burger(n-1,0))
    else:
        return 1 + 2*burger(n-1,0)
n,x = map(int,input().split())
print(burger(n,x))

if __name__ == '__main__':
    burger()