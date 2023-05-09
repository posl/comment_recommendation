def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            B = [x for x in A if x <= query[1]]
            B.sort(reverse=True)
            if len(B) >= query[2]:
                print(B[query[2]-1])
            else:
                print(-1)
        elif query[0] == 3:
            A.sort()
            B = [x for x in A if x >= query[1]]
            B.sort()
            if len(B) >= query[2]:
                print(B[query[2]-1])
            else:
                print(-1)
        else:
            print("error")
            break
