def main():
    S = input()
    print('Yes' if S[0].isupper() and S[1:7].isdigit() and S[7].isupper() and len(S)==8 else 'No')
