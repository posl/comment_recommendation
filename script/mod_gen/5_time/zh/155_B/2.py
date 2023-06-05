def isOk(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    else:
        return False
N = int(input())
A = list(map(int, input().split()))
flag = True
for i in range(N):
    if not isOk(A[i]):
        flag = False

if __name__ == '__main__':
    isOk()