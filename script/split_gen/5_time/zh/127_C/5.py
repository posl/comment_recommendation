def main():
    n, m = map(int, input().split())
    L = [0] * m
    R = [0] * m
    for i in range(m):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    if L[m - 1] > R[0]:
        print(0)
    else:
        print(R[0] - L[m - 1] + 1)
