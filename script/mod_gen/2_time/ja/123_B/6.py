def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    order_time = 0
    order_list = [A, B, C, D, E]
    order_list.sort()
    for i in range(0, 5):
        if order_time % 10 != 0:
            order_time += 10 - order_time % 10
        order_time += order_list[i]
    print(order_time)

if __name__ == '__main__':
    main()