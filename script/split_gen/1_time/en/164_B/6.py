def main():
    A, B, C, D = map(int, input().split())
    if B >= C * D:
        print('No')
    else:
        print('Yes')
