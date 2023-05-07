def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    ans = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        else:
            ans.append(A[query[1]-1])
    for i in ans:
        print(i)
