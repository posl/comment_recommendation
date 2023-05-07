def main():
    a, b, c = map(int, input().split())
    if b == min(a, b, c) or b == max(a, b, c):
        print('No')
    else:
        print('Yes')
