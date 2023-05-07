def main():
    N = int(input())
    A = []
    for i in range(N):
        Q = list(map(int, input().split()))
        if Q[0] == 1:
            A.append(Q[1])
        elif Q[0] == 2:
            A.sort()
            if len(A) == 0:
                print(-1)
            else:
                if Q[1] < A[0]:
                    print(-1)
                else:
                    if len(A) < Q[2]:
                        print(-1)
                    else:
                        print(A[-Q[2]])
        elif Q[0] == 3:
            A.sort(reverse=True)
            if len(A) == 0:
                print(-1)
            else:
                if Q[1] > A[0]:
                    print(-1)
                else:
                    if len(A) < Q[2]:
                        print(-1)
                    else:
                        print(A[-Q[2]])
