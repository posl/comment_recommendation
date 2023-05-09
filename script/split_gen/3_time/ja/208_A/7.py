def main():
    a, b = map(int, input().split())
    if a <= b <= a*6:
        print('Yes')
    else:
        print('No')
