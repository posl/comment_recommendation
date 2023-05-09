def main():
    #input
    S = input()
    #output
    if S[0].isupper() and S[1:7].isdigit() and int(S[1:7]) >= 100000 and int(S[1:7]) <= 999999 and S[7].isupper():
        print('Yes')
    else:
        print('No')
