def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(2*n)]
    for i in range(m):
        win = [0 for _ in range(2*n)]
        for j in range(n):
            if a[2*j][i] == a[2*j+1][i]:
                win[2*j] += 1
                win[2*j+1] += 1
            elif a[2*j][i] == "G" and a[2*j+1][i] == "C":
                win[2*j] += 3
            elif a[2*j][i] == "C" and a[2*j+1][i] == "P":
                win[2*j] += 3
            elif a[2*j][i] == "P" and a[2*j+1][i] == "G":
                win[2*j] += 3
            else:
                win[2*j+1] += 3
        a = [a[i] for i in sorted(range(2*n), key=lambda x: (-win[x], x))]
    for i in range(2*n):
        print(a[i])
