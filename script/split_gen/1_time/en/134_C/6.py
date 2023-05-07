def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    maxAidx = A.index(maxA)
    A.pop(maxAidx)
    maxA2 = max(A)
    for i in range(N):
        if i == maxAidx:
            print(maxA2)
        else:
            print(maxA)
