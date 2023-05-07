def highest_bridge(N, H):
    highest = H[0]
    highest_index = 0
    for i in range(1, N):
        if H[i] > highest:
            highest = H[i]
            highest_index = i
    return highest_index + 1
N = int(input())
H = list(map(int, input().split()))
print(highest_bridge(N, H))
