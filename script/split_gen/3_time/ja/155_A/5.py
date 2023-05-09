def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print('Yes')
    elif b == c and c != a:
        print('Yes')
    elif c == a and a != b:
        print('Yes')
    else:
        print('No')
