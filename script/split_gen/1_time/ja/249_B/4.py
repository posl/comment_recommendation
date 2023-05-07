def main():
    S = input()
    if len(S) >= 2 and len(S) <= 100:
        if S.islower() or S.isupper():
            print('No')
        else:
            if len(set(S)) == len(S):
                print('Yes')
            else:
                print('No')
    else:
        print('No')
