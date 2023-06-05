def max_move(stones, a_list):
    a_list = sorted(a_list)
    a_list.append(stones)
    a_list.insert(0, 0)
    max_move = 0
    for i in range(len(a_list) - 1):
        max_move = max(max_move, a_list[i + 1] - a_list[i])
    return max_move

if __name__ == '__main__':
    max_move()