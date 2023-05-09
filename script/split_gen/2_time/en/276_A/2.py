def main():
    S = input()
    if S.count('a') == 0:
        print(-1)
    else:
        print(len(S) - S[::-1].index('a') - 1)
