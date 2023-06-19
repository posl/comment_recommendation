def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = 0
    for i in range(n):
        if i == 0:
            min = p[i]
            count += 1
        else:
            if p[i] <= min:
                count += 1
                min = p[i]
    print(count)
