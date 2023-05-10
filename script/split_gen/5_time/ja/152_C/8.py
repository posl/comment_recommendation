def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_min = n+1
    count = 0
    for i in range(n):
        if p[i] <= p_min:
            count += 1
            p_min = p[i]
    print(count)
