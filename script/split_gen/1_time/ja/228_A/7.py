def main():
    S, T, X = map(int, input().split())
    if X < S:
        print('No')
    elif X >= T:
        print('No')
    else:
        print('Yes')
