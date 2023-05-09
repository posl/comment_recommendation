def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    p_list.sort(reverse=True)
    #print(p_list)
    total = 0
    for i in range(N-1):
        total += p_list[i]
    total += p_list[-1] / 2
    print(total)

if __name__ == '__main__':
    main()