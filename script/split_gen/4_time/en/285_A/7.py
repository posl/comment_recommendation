def main():
    a,b = map(int, input().split())
    if a>b:
        a,b = b,a
    if a+3>b:
        print('Yes')
    else:
        print('No')
