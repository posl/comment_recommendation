def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A = [str(a) for a in A]
    match = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
    ans = ""
    for i in range(9, 0, -1):
        if match[i] <= N and str(i) in A:
            ans += str(i) * (N // match[i])
            N %= match[i]
    print(ans)
