def main():
    S = input()
    if len(S) == 4 and len(set(S)) == 2 and S.count(S[0]) == 2:
        print('Yes')
    else:
        print('No')
