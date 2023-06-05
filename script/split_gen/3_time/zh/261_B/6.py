def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    flag = True
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == 'W' and A[j][i] != 'L':
                    flag = False
                    break
                elif A[i][j] == 'L' and A[j][i] != 'W':
                    flag = False
                    break
                elif A[i][j] == 'D' and A[j][i] != 'D':
                    flag = False
                    break
    if flag:
        print('正确')
    else:
        print('不正确')
