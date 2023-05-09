def main():
    import math
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if math.sqrt(i*j).is_integer():
                ans += 1
    print(ans)
