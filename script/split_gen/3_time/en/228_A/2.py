def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print('Yes')
    else:
        print('No')
