def main():
    n = int(input())
    v_list = list(map(int, input().split()))
    v_list.sort()
    result = v_list[0]
    for i in range(1, n):
        result = (result + v_list[i]) / 2
    print(result)

if __name__ == '__main__':
    main()