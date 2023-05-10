def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_orange = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(1, a[j]+1):
                orange = 0
                for l in range(i, j+1):
                    if a[l] >= k:
                        orange += k
                if orange > max_orange:
                    max_orange = orange
    print(max_orange)
