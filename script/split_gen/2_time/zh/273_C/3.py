def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    count = 0
    for i in range(N):
        if i == 0:
            print(0)
            continue
        elif A[i] == A[i-1]:
            print(count)
            continue
        else:
            count += 1
            print(count)
            continue
