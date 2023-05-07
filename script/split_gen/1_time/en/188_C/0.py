def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(1, 2 ** N + 1):
        B.append([i, A[i - 1]])
    while len(B) > 2:
        tmp = []
        for i in range(0, len(B), 2):
            if B[i][1] > B[i + 1][1]:
                tmp.append(B[i])
            else:
                tmp.append(B[i + 1])
        B = tmp
    if B[0][1] > B[1][1]:
        print(B[1][0])
    else:
        print(B[0][0])
