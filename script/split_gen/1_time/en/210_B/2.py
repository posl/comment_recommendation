def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == '1':
            print('Takahashi' if i % 2 == 0 else 'Aoki')
            break
