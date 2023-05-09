def main():
    n = int(input())
    A = []
    for i in range(n):
        s, p = input().split()
        A.append([s, int(p), i + 1])
    A.sort(key=lambda x: (-x[1], x[0], x[2]))
    for i in range(n):
        print(A[i][2])
