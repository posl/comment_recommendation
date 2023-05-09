def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print('Yes' if len(set(S)) == N else 'No')
