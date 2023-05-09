def main():
    S = input()
    if len(S) <= 100:
        if S[::2].count('R') + S[::2].count('U') + S[::2].count('D') == len(S[::2]):
            if S[1::2].count('L') + S[1::2].count('U') + S[1::2].count('D') == len(S[1::2]):
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
