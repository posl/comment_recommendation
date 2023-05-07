def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    S.sort()
    T.sort(reverse=True)
    if S < T:
        print('Yes')
    else:
        print('No')
