def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(30):
        cnt = 0
        for a in A:
            if a >> i & 1:
                cnt += 1
        ans |= (cnt % 2) << i
    print(ans)
