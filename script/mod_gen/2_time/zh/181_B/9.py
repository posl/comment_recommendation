def sum_of_integers_on_blackboard(n, a_list, b_list):
    sum = 0
    for i in range(n):
        sum += b_list[i] * (b_list[i] + 1) // 2
        sum -= a_list[i] * (a_list[i] - 1) // 2
    return sum

if __name__ == '__main__':
    sum_of_integers_on_blackboard()