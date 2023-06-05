def solve():
    answer = 0
    # 问题解决方案:
    # 1. 如果有200的倍数, 则必然存在两个数的差是200的倍数
    # 2. 如果两个数的差是200的倍数, 则这两个数对200取余数必然是相同的
    # 3. 因此, 可以遍历取余数, 然后统计每个余数的数目, 然后(1+2+...n-1)即为所求
    # 4. 注意, 如果余数是0, 则需要特殊处理, 因为0是所有数的倍数, 所以需要单独统计
    # 5. 注意, 如果余数是100, 则需要特殊处理, 因为100是所有数的倍数, 所以需要单独统计
    remainder_dict = {}
    for num in num_list:
        remainder = num % 200
        if remainder == 0:
            answer += remainder_dict.get(0, 0)
            remainder_dict[0] = remainder_dict.get(0, 0) + 1
        elif remainder == 100:
            answer += remainder_dict.get(100, 0)
            remainder_dict[100] = remainder_dict.get(100, 0) + 1
        else:
            answer += remainder_dict.get(remainder, 0)
            remainder_dict[remainder] = remainder_dict.get(remainder, 0) + 1
    return answer

if __name__ == '__main__':
    solve()