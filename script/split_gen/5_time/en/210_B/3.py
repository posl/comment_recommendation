def problems210_b():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:
                print('Takahashi')
            else:
                print('Aoki')
            break
