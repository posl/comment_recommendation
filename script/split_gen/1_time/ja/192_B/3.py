def main():
    S = input()
    if S[0::2].islower() and S[1::2].isupper():
        print('Yes')
    else:
        print('No')
