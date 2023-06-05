def main():
    n = int(input())
    a = list(map(int, input().split()))
    #a = [3, 2, 3, 2, 2]
    #a = [2, 3, 2, 3, 3, 3, 2, 3, 3, 2]
    b = []
    for i in range(n):
        b.append(0)
    for i in range(n):
        b[a[i]-1] += 1
    #print(b)
    for i in range(n):
        print(n - sum(b[0:a[i]]))
