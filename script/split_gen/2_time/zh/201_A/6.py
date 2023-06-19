def problems201_a():
    A = input("请输入三个数字，以空格分隔：")
    A = A.split(' ')
    A = [int(i) for i in A]
    A.sort()
    if (A[2] - A[1]) == (A[1] - A[0]):
        print("Yes")
    else:
        print("No")
    return None
