def main():
    N = int(input())
    N_list = list(str(N))
    N_len = len(N_list)
    N_first = int(N_list[0])
    if N_len == 1:
        print(N)
    else:
        N_len -= 1
        N_first -= 1
        N_first *= 9
        N_first += int("".join(N_list[1:])) + 1
        print(N_first + (N_len * 9))
