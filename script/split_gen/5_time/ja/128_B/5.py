def main():
    N = int(input())
    arr = []
    for i in range(N):
        s, p = input().split()
        arr.append((s, int(p), i+1))
    arr = sorted(arr, key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(arr[i][2])
