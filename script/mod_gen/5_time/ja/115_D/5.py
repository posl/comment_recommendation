def burger(l,x):
    if l == 0:
        return 1
    elif x == 1:
        return 0
    elif x <= 1 + burger(l-1,x-1):
        return burger(l-1,x-1)
    elif x == 2 + burger(l-1,x-2):
        return 1 + burger(l-1,x-2)
    elif x <= 2 + 2*burger(l-1,x-2):
        return 1 + burger(l-1,x-2)
    else:
        return 2 + 2*burger(l-1,x-2)
l,x = map(int,input().split())
print(burger(l,x))

if __name__ == '__main__':
    burger()