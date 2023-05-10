def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%200 for a in A]
    count = [0]*200
    for a in A:
        count[a] += 1
    ans = 0
    for c in count:
        ans += c*(c-1)//2
    print(ans)
