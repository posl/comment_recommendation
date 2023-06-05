def main():
    num = int(input())
    input_list = list(map(int, input().split()))
    for i in range(num):
        if input_list[i] == i+1:
            continue
        else:
            if input_list[i] == i+2 and input_list[i+1] == i+1:
                continue
            else:
                print('NO')
                return
    print('YES')
    return

if __name__ == '__main__':
    main()