def get_max_cheese(n, w, cheese_list):
    cheese_list.sort(key=lambda x:x[0]/x[1], reverse=True)
    sum_cheese = 0
    for cheese in cheese_list:
        if cheese[1] < w:
            sum_cheese += cheese[0]
            w -= cheese[1]
        else:
            sum_cheese += cheese[0]/cheese[1]*w
            break
    return sum_cheese

if __name__ == '__main__':
    get_max_cheese()