def main():
    a,b,c = map(int, input().split())
    if a*a + b*b < c*c:
        print('Yes')
    else:
        print('No')
