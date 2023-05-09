def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    count = 0
    while True:
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            elif A[i] % 3 == 0:
                A[i] = A[i] / 3
            else:
                print(-1)
                return
        if len(set(A)) == 1:
            print(count)
            return
        count += 1
