def get_min_mp(input_list):
    # input_list = [5, 100, 90, 80, 98, 40, 30, 21, 80]
    # input_list = [8, 100, 90, 80, 100, 100, 90, 90, 90, 80, 80, 80]
    # input_list = [8, 1000, 800, 100, 300, 333, 400, 444, 500, 555, 600, 666]
    N = input_list[0]
    A = input_list[1]
    B = input_list[2]
    C = input_list[3]
    l = input_list[4:]
    l.sort(reverse=True)
    # print l

if __name__ == '__main__':
    get_min_mp()