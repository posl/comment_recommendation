def main():
    a,b,c,d,e = map(int, input().split())
    if a != b and a != c and a != d and a != e and b != c and b != d and b != e and c != d and c != e and d != e:
        print(5)
    elif a == b and a == c and a == d and a == e and b == c and b == d and b == e and c == d and c == e and d == e:
        print(1)
    else:
        print(4)
