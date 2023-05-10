def full_house(a, b, c, d, e):
    if a == b == c and d == e:
        print("Yes")
    elif a == b and c == d == e:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    full_house()