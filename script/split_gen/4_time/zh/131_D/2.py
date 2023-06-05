def main():
    n = int(input())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = list(zip(A, B))
    C.sort(key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += C[i][0]
        if t > C[i][1]:
            print("No")
            exit()
    print("Yes")
