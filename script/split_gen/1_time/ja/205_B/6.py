def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [i for i in range(1, N+1)]
    if A == B:
        print('Yes')
    else:
        print('No')
