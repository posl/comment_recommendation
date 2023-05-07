def main():
    S = input()
    T = input()
    S = sorted(S)
    T = sorted(T, reverse=True)
    print('Yes' if S < T else 'No')
