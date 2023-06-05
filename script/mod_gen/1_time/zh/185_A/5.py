def problem185_a():
    A = input().split()
    A = list(map(int, A))
    A.sort()
    print(A[0])

if __name__ == '__main__':
    problem185_a()