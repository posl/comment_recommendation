def main():
    N = int(input())
    A = list(map(int,input().split()))
    count = [0]*(N+1)
    for a in A:
        count[a] += 1
    ans = 0
    for c in count:
        ans += c*(c-1)//2
    for a in A:
        print(ans-count[a]+1)
