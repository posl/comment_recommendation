def problem185_a():
    A = input().split()
    A = [int(x) for x in A]
    A.sort()
    if A[3] - A[0] <= 3:
        print("YES")
    else:
        print("NO")
