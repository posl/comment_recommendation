def main():
    a, b = map(int, input().split())
    if a < 1 or b > 15 or a >= b:
        return
    if b - a == 1:
        print('Yes')
    else:
        print('No')
