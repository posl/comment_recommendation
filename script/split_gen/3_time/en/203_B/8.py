def sum_room_number():
    N, K = map(int, input().split())
    print(N * 100 * K + K * (K + 1) // 2)
sum_room_number()
