def get_input():
    h, w = map(int, input().split())
    input_list = []
    for i in range(h):
        input_list.append(input())
    return h, w, input_list

if __name__ == '__main__':
    get_input()