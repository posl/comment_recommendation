def main():
    S = input()
    if S[0] == '0':
        print('No')
        exit()
    for i in range(1, 9):
        if S[i] == '1' and S[i-1] == '0' and S[i+1] == '0':
            print('Yes')
            exit()
    print('No')
    exit()
