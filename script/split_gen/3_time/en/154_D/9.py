def dice(dice, k):
    if k == 1:
        return max(dice)
    else:
        return max(dice) + dice(dice[1:], k-1)
n, k = map(int, input().split())
dice = list(map(int, input().split()))
print(dice(dice, k)/2)
