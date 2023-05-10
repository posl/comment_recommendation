def main():
    n, x = map(int, input().split())
    bags = []
    for _ in range(n):
        bags.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 2**n):
        tmp = i
        sum = 1
        for j in range(n):
            if tmp % 2 == 1:
                sum *= bags[j][0]
            tmp //= 2
        if sum == x:
            ans += 1
    print(ans)
