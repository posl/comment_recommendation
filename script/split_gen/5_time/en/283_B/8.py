def solution(input):
    n = input[0]
    a = input[1]
    q = input[2]
    for i in range(q):
        if input[3 + i][0] == 1:
            a[input[3 + i][1] - 1] = input[3 + i][2]
        else:
            print(a[input[3 + i][1] - 1])
