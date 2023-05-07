def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    while i < N:
        if i % 2 == 0:
            X -= A[i]
        i += 1
    
    if X >= 0:
        print('Yes')
    else:
        print('No')
