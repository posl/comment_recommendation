def main():
    a, b, c = map(int, input().split())
    if a < b < c or c < b < a:
        print('Yes')
    elif a < c < b or b < c < a:
        print('Yes')
    else:
        print('No')
