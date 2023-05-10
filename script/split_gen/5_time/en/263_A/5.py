def main():
    a,b,c,d,e = map(int, input().split())
    if (a == b and c == d == e) or (a == c and b == d == e) or (a == d and b == c == e) or (a == e and b == c == d) or (b == c and a == d == e) or (b == d and a == c == e) or (b == e and a == c == d) or (c == d and a == b == e) or (c == e and a == b == d) or (d == e and a == b == c):
        print('Yes')
    else:
        print('No')
