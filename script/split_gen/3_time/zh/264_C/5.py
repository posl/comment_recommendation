def main():
    h1, w1 = map(int, input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int, input().split())))
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if A[i][j] == B[0][0]:
                if A[i:h2 + i] == B:
                    print("Yes")
                    exit()
    print("No")
