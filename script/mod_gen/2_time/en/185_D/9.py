def get_num_of_stamps(num_of_squares, num_of_blue_squares, blue_squares):
    if num_of_blue_squares == 0:
        return 1
    if num_of_squares == num_of_blue_squares:
        return 0
    blue_squares.sort()
    max_distance = 0
    for i in range(num_of_blue_squares - 1):
        max_distance = max(max_distance, blue_squares[i + 1] - blue_squares[i])
    return (max_distance + 1) // 2 + 1
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(get_num_of_stamps(N, M, A))

if __name__ == '__main__':
    get_num_of_stamps()