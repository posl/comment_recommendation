def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    flag = True
    for i in range(N):
        if i+1 != A[i]:
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No')
