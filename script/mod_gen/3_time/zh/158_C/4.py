def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
import math
a, b = map(int, input().split())
n = 1
while True:
    if round_up(n * 0.08) == a and round_up(n * 0.1) == b:
        print(n)
        break
    elif round_up(n * 0.08) > a or round_up(n * 0.1) > b:
        print(-1)
        break
    else:
        n += 1

if __name__ == '__main__':
    round_up()