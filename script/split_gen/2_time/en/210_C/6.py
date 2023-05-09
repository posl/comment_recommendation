def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    #print(N, K, C)
    #print(len(C))
    max_kinds = 0
    kinds = 0
    for i in range(N):
        if not C[i] in C[i-K:i]:
            kinds += 1
        if kinds > max_kinds:
            max_kinds = kinds
        if i >= K-1:
            if not C[i-K+1] in C[i-K+2:i+1]:
                kinds -= 1
    print(max_kinds)
