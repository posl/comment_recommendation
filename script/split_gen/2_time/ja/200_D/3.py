def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]].append(i)
        else:
            d[A[i]] = [i]
    for k in d:
        if len(d[k]) > 1:
            print("Yes")
            print(1, d[k][0] + 1)
            print(1, d[k][1] + 1)
            return
    for i in range(200):
        for j in range(i + 1, 200):
            if i in d and j in d:
                print("Yes")
                print(2, d[i][0] + 1, d[j][0] + 1)
                print(2, d[i][1] + 1, d[j][1] + 1)
                return
    print("No")
main()
