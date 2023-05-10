def main():
    S = input()
    if S[0].isupper() and S[7].isupper() and S[1:7].isdecimal():
        print('Yes')
    else:
        print('No')
