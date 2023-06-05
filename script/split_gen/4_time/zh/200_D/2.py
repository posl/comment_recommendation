def main():
    N = int(input())
    A = list(map(int, input().split()))
    for x in range(1, N+1):
        for y in range(1, N+1):
            B = [i for i in range(1, N+1) if i not in range(x+1, N+1)]
            C = [i for i in range(1, N+1) if i not in range(y+1, N+1)]
            if sum([A[i-1] for i in B]) % 200 == sum([A[i-1] for i in C]) % 200:
                print('Yes')
                print(len(B), ' '.join(map(str, B)))
                print(len(C), ' '.join(map(str, C)))
                return
    print('No')
