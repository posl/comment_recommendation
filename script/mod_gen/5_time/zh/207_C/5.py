def get_input():
    N = int(input())
    input_list = []
    for i in range(N):
        input_list.append(input().split())
    return N, input_list

if __name__ == '__main__':
    get_input()