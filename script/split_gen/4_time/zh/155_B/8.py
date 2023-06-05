def main():
    N = int(input())
    A = input().split()
    flag = True
    for i in range(N):
        if int(A[i])%2 == 0:
            if (int(A[i])%3 != 0) and (int(A[i])%5 != 0):
                flag = False
                break
    if flag:
        print('APPROVED')
    else:
        print('DENIED')
