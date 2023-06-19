def get_input():
    #get N
    N = int(input())
    #get T_i
    T_i = list(map(int, input().split()))
    return N, T_i

if __name__ == '__main__':
    get_input()