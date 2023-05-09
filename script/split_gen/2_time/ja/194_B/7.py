def main():
    N = int(input())
    A_B = []
    for i in range(N):
        A, B = map(int, input().split())
        A_B.append((A, B))
    A_B.sort(key=lambda x: x[0])
    A_B.sort(key=lambda x: x[1])
    print(max(A_B[0][1], A_B[1][0]))
