def main():
    S = input()
    if S[0].isupper() and S[-1].isupper() and len(S) == 8 and S[1:7].isdigit():
        print('Yes')
    else:
        print('No')
