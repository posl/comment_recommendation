def get_input():
    n = int(input())
    input_list = []
    for i in range(n):
        t, l, r = map(int, input().split())
        input_list.append((t, l, r))
    return input_list

if __name__ == '__main__':
    get_input()