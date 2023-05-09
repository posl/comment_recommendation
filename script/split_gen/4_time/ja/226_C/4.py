def main():
    N = int(input())
    T_list = []
    A_list = []
    for i in range(N):
        T_list.append(0)
        A_list.append([])
    for i in range(N):
        tmp = list(map(int,input().split()))
        T_list[i] = tmp[0]
        if tmp[1] != 0:
            A_l
