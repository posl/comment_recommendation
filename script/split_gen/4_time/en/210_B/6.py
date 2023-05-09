def main():
    N = int(input())
    S = input()
    for i in range(len(S)):
        if S[i] == '1':
            if (i + 1) % 2 == 1:
                print('Takahashi')
            else:
                print('Aoki')
            break
