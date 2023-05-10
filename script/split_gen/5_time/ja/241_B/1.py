def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                b[j] = 0
                break
        else:
            print("No")
            exit()
    print("Yes")
