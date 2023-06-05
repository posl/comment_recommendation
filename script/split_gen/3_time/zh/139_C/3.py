def main():
    n = int(input())
    H = [int(x) for x in input().split()]
    count = 0
    max_count = 0
    for i in range(n-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)
