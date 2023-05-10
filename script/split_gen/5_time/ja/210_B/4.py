def main():
    N = int(input())
    S = input()
    if S.count('1') % 2 == 1:
        print('Takahashi')
    else:
        print('Aoki')
