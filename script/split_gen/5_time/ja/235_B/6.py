def main():
    N = int(input())
    H = list(map(int, input().split()))
    
    count = 0
    for i in range(N-1, 0, -1):
        if H[i] >= H[i-1]:
            count += 1
        else:
            count = 0
        if count >= 2:
            print(H[i])
            break
    if count < 2:
        print(H[0])
