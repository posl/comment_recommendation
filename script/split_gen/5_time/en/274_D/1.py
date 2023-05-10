def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    a.append(0)
    for i in range(1, n+1):
        for j in range(i+1, n+2):
            if abs(a[j] - a[i]) + abs(j - i) == abs(y - x):
                print("Yes")
                exit()
    print("No")
