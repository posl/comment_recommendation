def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if N == K:
        if len(set(A)) == 1:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')
