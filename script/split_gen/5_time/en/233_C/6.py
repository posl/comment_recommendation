def main():
    N, X = map(int, input().split())
    bags = []
    for i in range(N):
        bags.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1, X + 1):
        if X % i == 0 and X // i <= 10**9:
            for bag in bags:
                if i in bag:
                    break
            else:
                continue
            for bag in bags:
                if X // i in bag:
                    ans += 1
                    break
    print(ans)
