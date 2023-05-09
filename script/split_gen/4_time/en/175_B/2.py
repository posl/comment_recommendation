def main():
    n = int(input())
    sticks = list(map(int, input().split()))
    sticks.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if sticks[i] != sticks[j] and sticks[j] != sticks[k] and sticks[k] != sticks[i]:
                    if sticks[i] + sticks[j] > sticks[k]:
                        count += 1
    print(count)
