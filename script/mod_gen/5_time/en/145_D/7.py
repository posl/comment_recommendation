def knight(x,y):
    if x == 1 and y == 1:
        return 0
    elif x == 1 or y == 1:
        return 1
    else:
        return 2
x,y = map(int, input().split())
print(knight(x,y))

if __name__ == '__main__':
    knight()