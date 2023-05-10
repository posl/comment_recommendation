def main():
    N, K = map(int, input().split())
    room_num = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            room_num += 100*i + j
    print(room_num)
