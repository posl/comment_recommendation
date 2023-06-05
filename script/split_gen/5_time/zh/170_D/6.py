def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i != j and a[j] % a[i] == 0:
                break
        else:
            cnt += 1
    print(cnt)
