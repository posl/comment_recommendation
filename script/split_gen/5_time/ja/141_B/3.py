def main():
    S = input()
    for i in range(0, len(S)):
        if i % 2 == 0 and S[i] == 'L':
            print('No')
            return
        if i % 2 == 1 and S[i] == 'R':
            print('No')
            return
    print('Yes')