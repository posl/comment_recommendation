def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_list = list(N_str)
    N_list.sort(reverse=True)
    N_list = [int(n) for n in N_list]
    #print(N_list)
    ans = 0
    for i in range(1, N_len):
        num1 = 0
        num2 = 0
        for j in range(N_len):
            if j < i:
                num1 = num1 * 10 + N_list[j]
            else:
                num2 = num2 * 10 + N_list[j]
        #print(num1, num2)
        if ans < num1 * num2:
            ans = num1 * num2
    print(ans)
main()
