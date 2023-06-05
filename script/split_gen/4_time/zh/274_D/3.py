def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(0)
    a.insert(0, 0)
    a.insert(0, 0)
    for i in range(1, n+2):
        for j in range(i+1, n+2):
            if a[i] + a[j] == abs(x) and a[i] * a[j] == abs(y):
                print('Yes')
                exit()
    print('No')
