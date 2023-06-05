def input():
    input_str = input()
    input_list = input_str.split(' ')
    N = int(input_list[0])
    K = int(input_list[1])
    L = []
    R = []
    for i in range(K):
        input_str = input()
        input_list = input_str.split(' ')
        L.append(int(input_list[0]))
        R.append(int(input_list[1]))
    return N, K, L, R

if __name__ == '__main__':
    input()