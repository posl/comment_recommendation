def main():
    N = int(input())
    A = input().split()
    B = input().split()
    for i in range(N):
        A[i] = int(A[i])
        B[i] = int(B[i])
    count = 0
    for x in range(1,1001):
        flag = True
        for i in range(N):
            if A[i] > x or B[i] < x:
                flag = False
                break
        if flag == True:
            count += 1
    print(count)
