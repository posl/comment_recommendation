def get_odd_num(num_list):
    odd_num = 0
    for i in num_list:
        if i % 2 != 0:
            odd_num += 1
    return odd_num
test_num = int(input())
for i in range(test_num):
    num = int(input())
    num_list = list(map(int, input().split()))
    print(get_odd_num(num_list))
