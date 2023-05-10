def main():
    N = int(input())
    A = list(map(int, input().split()))
    min = 0
    max = 0
    count = 0
    for i in range(N):
        if i+1 == A[i]:
            if min == 0:
                min = i+1
                max = i+1
            else:
                max = i+1
        elif i+1 < A[i]:
            if min == 0:
                min = i+1
                max = A[i]
            else:
                if min <= A[i]:
                    count += 1
                max = A[i]
        else:
            if min == 0:
                min = A[i]
                max = i+1
            else:
                if min <= i+1:
                    count += 1
                max = i+1
    print(count)
