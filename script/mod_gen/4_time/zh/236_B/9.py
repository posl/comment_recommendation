def solve(n, a):
    count = {}
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in count:
        if count[i] % 2 == 1:
            return i
    return 0
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
