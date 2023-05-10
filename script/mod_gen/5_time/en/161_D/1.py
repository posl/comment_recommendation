def solve(k):
    lunlun = [1,2,3,4,5,6,7,8,9]
    for _ in range(k-1):
        x = lunlun.pop(0)
        if x%10 != 0:
            lunlun.append(10*x + x%10 - 1)
        lunlun.append(10*x + x%10)
        if x%10 != 9:
            lunlun.append(10*x + x%10 + 1)
    return lunlun[0]
k = int(input())
print(solve(k))

if __name__ == '__main__':
    solve()