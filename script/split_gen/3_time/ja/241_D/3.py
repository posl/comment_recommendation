def main():
    N = int(input())
    A = []
    for i in range(N):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            A = list(reversed(A))
            if len(A) >= query[2]:
                print(A[query[2]-1])
            else:
                print("-1")
        elif query[0] == 3:
            A.sort()
            if len(A) >= query[2]:
                print(A[query[2]-1])
            else:
                print("-1")
        else:
            print("Error")
            break
