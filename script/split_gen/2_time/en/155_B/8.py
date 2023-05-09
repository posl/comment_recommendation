def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    for i in range(0, N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                continue
            else:
                print('DENIED')
                return
    print('APPROVED')
