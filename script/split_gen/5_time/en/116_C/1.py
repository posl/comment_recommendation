def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    while max(h) > 0:
        for i in range(n):
            if h[i] > 0:
                h[i] -= 1
                if i == n-1 or h[i+1] == 0:
                    count += 1
    print(count)
