def main():
    S = input()
    print('Yes' if len(set(S)) == 2 and S.count(S[0]) == 2 else 'No')
