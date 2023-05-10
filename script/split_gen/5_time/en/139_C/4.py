def main():
    N = int(input())
    H = list(map(int, input().split()))
    result = 0
    count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            result = max(result, count)
            count = 0
    result = max(result, count)
    print(result)
