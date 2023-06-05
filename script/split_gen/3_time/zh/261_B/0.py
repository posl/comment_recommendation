def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    flag = False
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                flag = True
                break
            if A[i][j] == 'L' and A[j][i] != 'W':
                flag = True
                break
            if A[i][j] == 'D' and A[j][i] != 'D':
                flag = True
                break
        if flag:
            break
    if flag:
        print('不正确')
    else:
        print('正确')
