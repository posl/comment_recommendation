def is_contain_7(num):
    while True:
        if num % 10 == 7:
            return True
        num = num // 10
        if num == 0:
            return False
print('是' if is_contain_7(int(input())) else '否')
