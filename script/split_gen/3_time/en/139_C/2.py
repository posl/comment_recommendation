def main():
    N = int(input())
    H = list(map(int, input().split()))
    
    count = 0
    max_count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        max_count = max(count, max_count)
    print(max_count)
