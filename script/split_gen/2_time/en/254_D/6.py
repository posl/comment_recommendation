def main():
    import math
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N:
                if math.sqrt(i*j).is_integer():
                    ans += 1
            else:
                break
    print(ans)
