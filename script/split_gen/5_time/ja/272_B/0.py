def main():
    n, m = map(int, input().split())
    k = []
    x = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(m):
        for j in range(i+1, m):
            if len(set(x[i]) & set(x[j])) >= 2:
                print("Yes")
                return
    print("No")
