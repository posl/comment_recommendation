def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_list = list(N_str)
    N_list.sort(reverse=True)
    N_list = list(map(int, N_list))
    N_list_sum = sum(N_list)
    if N_list_sum % 3 == 0:
        print(0)
    else:
        for i in range(N_len):
            if (N_list_sum - N_list[i]) % 3 == 0:
                print(1)
                break
            else:
                print(-1)
                break
