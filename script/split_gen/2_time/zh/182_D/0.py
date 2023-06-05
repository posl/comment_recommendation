def main():
    N = int(input())
    N_list = list(str(N))
    N_list.sort(reverse=True)
    N = int(''.join(N_list))
    for i in range(len(N_list)):
        if N % 3 == 0:
            print(i)
            return
        else:
            N_list.pop(i)
            N = int(''.join(N_list))
    print(-1)
