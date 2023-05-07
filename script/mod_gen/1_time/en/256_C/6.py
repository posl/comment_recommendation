def main():
    h_list = list(map(int, input().split()))
    w_list = list(map(int, input().split()))
    count = 0
    for x in range(1, 31):
        for y in range(1, 31):
            for z in range(1, 31):
                if h_list[0] == x + y + z and h_list[1] == x + 2 * y + 3 * z and h_list[2] == 3 * x + 2 * y + z:
                    if w_list[0] == x + 2 * y + 3 * z and w_list[1] == 4 * x + 2 * y + z and w_list[2] == 3 * x + 2 * y + 4 * z:
                        count += 1
    print(count)

if __name__ == '__main__':
    main()