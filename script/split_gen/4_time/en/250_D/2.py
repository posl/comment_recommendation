def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N ** (1 / 3)) + 1):
        for j in range(2, int(N ** (1 / 6)) + 1):
            if i ** 3 * j > N:
                break
            ans += 1
    print(ans)
main()
import sys
import math
