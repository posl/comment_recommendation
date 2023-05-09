def comma_count(n):
    # n以下の整数を1度ずつ書くとき、コンマは合計で何回書かれるか
    if n < 1000:
        return 0
    else:
        return n//1000 + comma_count(n//1000)
n = int(input())
print(comma_count(n))
