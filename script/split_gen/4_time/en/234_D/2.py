def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    for i in range(k-1, n):
        ans.append(sorted(p[:i+1])[k-1])
    print(*ans, sep='\n')
