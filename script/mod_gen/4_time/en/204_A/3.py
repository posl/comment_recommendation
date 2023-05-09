def hand(x, y):
    if x == y:
        return x
    elif x == 0 and y == 1:
        return x
    elif x == 1 and y == 0:
        return y
    elif x == 0 and y == 2:
        return y
    elif x == 2 and y == 0:
        return x
    elif x == 1 and y == 2:
        return x
    elif x == 2 and y == 1:
        return y
x, y = input().split()
print(hand(x, y))

if __name__ == '__main__':
    hand()