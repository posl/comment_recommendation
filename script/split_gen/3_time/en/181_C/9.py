def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    result = "No"
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (x[j] - x[i]) * (y[k] - y[i]) == (x[k] - x[i]) * (y[j] - y[i]):
                    result = "Yes"
                    break
            else:
                continue
            break
        else:
            continue
        break
    print(result)
