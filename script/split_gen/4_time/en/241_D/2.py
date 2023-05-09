def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            A = sorted(A)
            x = int(query[1])
            k = int(query[2])
            if k > len(A):
                print(-1)
            else:
                cnt = 0
                for j in range(len(A)):
                    if A[j] <= x:
                        cnt += 1
                        if cnt == k:
                            print(A[j])
                            break
        elif query[0] == '3':
            A = sorted(A,reverse=True)
            x = int(query[1])
            k = int(query[2])
            if k > len(A):
                print(-1)
            else:
                cnt = 0
                for j in range(len(A)):
                    if A[j] >= x:
                        cnt += 1
                        if cnt == k:
                            print(A[j])
                            break
