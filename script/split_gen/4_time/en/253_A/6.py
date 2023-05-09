def main():
    a, b, c = map(int, input().split())
    if b in [a, c]:
        print('Yes')
    else:
        print('No')
