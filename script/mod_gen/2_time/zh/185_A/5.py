def get_max_contest_num(a1, a2, a3, a4):
    a_sum = a1 + a2 + a3 + a4
    if a_sum % 100 != 0:
        return 0
    else:
        return 1
a1, a2, a3, a4 = map(int, input().split())
print(get_max_contest_num(a1, a2, a3, a4))
