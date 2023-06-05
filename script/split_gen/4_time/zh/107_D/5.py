def main():
    N = int(input())
    a = list(map(int, input().split()))
    # a = [10, 30, 20]
    # a = [10]
    # a = [5, 9, 5, 9, 8, 9, 3, 5, 4, 3]
    b = []
    for i in range(N):
        for j in range(i, N):
            b.append(a[i:j+1])
    # print(b)
    c = []
    for i in range(len(b)):
        c.append(sorted(b[i])[len(b[i])//2])
    # print(c)
    print(sorted(c)[len(c)//2])
