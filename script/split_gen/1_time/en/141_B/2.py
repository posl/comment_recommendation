def main():
    S = input()
    if all([S[i] in 'RUD' for i in range(len(S)) if i % 2 == 0]) and all([S[i] in 'LUD' for i in range(len(S)) if i % 2 == 1]):
        print('Yes')
    else:
        print('No')
