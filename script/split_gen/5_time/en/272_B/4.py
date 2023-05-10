def main():
    n, m = map(int, input().split())
    k = []
    x = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(m):
        for j in range(m):
            if i != j:
                if len(set(x[i]) & set(x[j])) > 0:
                    x[i] = list(set(x[i]) | set(x[j]))
    if len(set(x[0])) == n:
        print("Yes")
    else:
        print("No")
