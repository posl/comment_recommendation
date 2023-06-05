def main():
    N = int(input())
    if N%3 == 0:
        print(0)
        return
    N_list = list(str(N))
    N_list.sort()
    N_list.reverse()
    #print(N_list)
    sum_N = sum(map(int,N_list))
    #print(sum_N)
    for i in range(len(N_list)):
        if (sum_N-int(N_list[i]))%3 == 0:
            print(i+1)
            return
    print(-1)
