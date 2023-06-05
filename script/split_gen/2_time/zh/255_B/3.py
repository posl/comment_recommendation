def main():
    r, c = map(int, input().split())
    a = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        a[i] = list(map(int, input().split()))
    print(a[r-1][c-1])
