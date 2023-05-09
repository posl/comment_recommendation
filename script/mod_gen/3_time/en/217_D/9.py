def get_input():
    input_line = input()
    input_line = input_line.split(" ")
    l = int(input_line[0])
    q = int(input_line[1])
    queries = []
    for i in range(q):
        input_line = input()
        input_line = input_line.split(" ")
        queries.append((int(input_line[0]), int(input_line[1])))
    return l, q, queries

if __name__ == '__main__':
    get_input()