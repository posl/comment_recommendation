def calc_cost(cost_list, book_list):
    total_cost = 0
    for i in range(len(book_list)):
        total_cost += cost_list[i] * book_list[i]
    return total_cost
