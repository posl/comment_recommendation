def main():
    S = input()
    if len(set(S)) != len(S) or S.islower():
        print('No')
    else:
        print('Yes')
