def get_list():
    n_x = input()
    n_x = n_x.split(' ')
    n = int(n_x[0])
    x = int(n_x[1])
    bag = []
    for i in range(n):
        bag.append(input())
    return n,x,bag
