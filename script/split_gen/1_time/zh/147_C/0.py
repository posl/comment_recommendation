def input_data():
    input_data = []
    N = int(input())
    for i in range(N):
        A = int(input())
        input_data.append(A)
        for j in range(A):
            input_data.append(list(map(int,input().split())))
    return input_data
