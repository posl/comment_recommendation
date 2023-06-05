def count_odd():
    num = int(input())
    num_list = input().split()
    count = 0
    for i in range(num):
        if int(num_list[i]) % 2 != 0:
            count += 1
    print(count)

if __name__ == '__main__':
    count_odd()