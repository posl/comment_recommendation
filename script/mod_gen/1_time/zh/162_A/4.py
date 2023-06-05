def is_contain_seven(num):
    return num % 10 == 7 or num // 10 % 10 == 7 or num // 100 == 7
num = int(input())
print("是" if is_contain_seven(num) else "否")
