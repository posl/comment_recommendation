def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    count = 0
    max_count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)
