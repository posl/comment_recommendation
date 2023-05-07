def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            ans = 0
            for i in range(len(A)):
                if A[i] > query[1]:
                    ans = A[i-1]
                    break
            if ans == 0:
                ans = A[-1]
            print(ans)
        elif query[0] == 3:
            A.sort()
            ans = 0
            for i in range(len(A)):
                if A[i] >= query[1]:
                    ans = A[i]
                    break
            if ans == 0:
                ans = -1
            print(ans)
