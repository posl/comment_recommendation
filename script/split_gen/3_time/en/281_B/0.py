def main():
    S = input()
    if S[0].isupper() and S[1:7].isdigit() and S[7].isupper():
        print('Yes')
    else:
        print('No')
