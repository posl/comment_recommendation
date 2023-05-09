def main():
    import sys
    import math
    n = int(input())
    ans = 0
    for i in range(1, int(math.sqrt(n))+1):
        for j in range(1, int(math.sqrt(n))+1):
            for k in range(1, int(math.sqrt(n))+1):
                if i*j*k <= n:
                    if i == j and j == k:
                        ans += 1
                    elif i == j or j == k:
                        ans += 3
                    else:
                        ans += 6
                else:
                    break
    print(ans)

if __name__ == '__main__':
    main()