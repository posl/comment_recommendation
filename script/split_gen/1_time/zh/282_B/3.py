def get_input():
    input_line = input().split()
    n = int(input_line[0])
    m = int(input_line[1])
    s = [input() for i in range(n)]
    return n, m, s
