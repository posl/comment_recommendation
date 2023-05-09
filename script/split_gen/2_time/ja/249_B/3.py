def main():
    S = input()
    if S.islower() or S.isupper():
        print('No')
    else:
        if len(set(S)) == len(S):
            print('Yes')
        else:
            print('No')
