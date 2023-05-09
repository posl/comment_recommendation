def main():
    K = int(input())
    ans = 0
    ans_list = []
    for i in range(1, 10):
        ans_list.append(i)
    while len(ans_list) < K:
        ans = ans_list.pop(0)
        for i in range(-1, 2):
            if 0 <= ans % 10 + i <= 9:
                ans_list.append(ans * 10 + ans % 10 + i)
    print(ans_list[K - 1])

if __name__ == '__main__':
    main()