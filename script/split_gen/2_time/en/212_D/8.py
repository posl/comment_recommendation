def main():
    Q = int(input())
    A = []
    for i in range(Q):
        a,b = map(int, input().split())
        A.append([a,b])
    
    ans = []
    min = 0
    add = 0
    for i in range(Q):
        if A[i][0] == 1:
            A[i][1] -= add
            if A[i][1] < min:
                min = A[i][1]
        elif A[i][0] == 2:
            add += A[i][1]
        else:
            ans.append(min+add)
            min += add
            add = 0
    for i in ans:
        print(i)
