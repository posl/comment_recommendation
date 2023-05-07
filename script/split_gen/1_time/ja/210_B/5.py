def main():
    N = int(input())
    S = input()
    if S[0] == '0':
        print('Takahashi')
    else:
        if S.count('0') > 0:
            print('Takahashi')
        else:
            print('Aoki')
