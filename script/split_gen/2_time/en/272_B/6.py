def main():
    N, M = map(int, input().split())
    for i in range(M):
        input() # k_i
        if len(set(input().split())) == N:
            print('No')
            return
    print('Yes')
