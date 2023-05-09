def main():
    S = input()
    if S[0] == '0':
        if S[1] == '0':
            print('No')
        else:
            if S[4] == '0' or S[5] == '0':
                print('Yes')
            else:
                print('No')
    else:
        if S[4] == '0':
            if S[5] == '0':
                print('No')
            else:
                print('Yes')
        else:
            if S[1] == '0' or S[2] == '0':
                print('Yes')
            else:
                print('No')
