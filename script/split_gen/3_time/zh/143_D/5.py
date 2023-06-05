def main():
    n = int(input())
    sticks = [int(x) for x in input().split()]
    sticks.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if sticks[i] + sticks[j] > sticks[k]:
                    count += 1
    print(count)
