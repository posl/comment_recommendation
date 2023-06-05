def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if x[i] == x[j] or y[i] == y[j]:
                for k in range(j+1,N):
                    if x[i] == x[j] and x[j] == x[k]:
                        for l in range(k+1,N):
                            if y[i] == y[k] and y[j] == y[l]:
                                ans += 1
                    elif y[i] == y[j] and y[j] == y[k]:
                        for l in range(k+1,N):
                            if x[i] == x[k] and x[j] == x[l]:
                                ans += 1
    print(ans)
