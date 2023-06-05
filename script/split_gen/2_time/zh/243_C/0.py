def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt1 += 1
        for j in range(n):
            if a[i] == b[j]:
                cnt2 += 1
    print(cnt1)
    print(cnt2 - cnt1)
