def main():
    N = int(input())
    S = input()
    #print(N, S)
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:
                print('Takahashi')
            else:
                print('Aoki')
            break
