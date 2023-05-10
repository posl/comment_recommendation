def problems103_a():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])

if __name__ == '__main__':
    problems103_a()