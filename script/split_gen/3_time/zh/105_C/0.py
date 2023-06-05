def main():
    num = int(input())
    if num == 0:
        print(0)
        return
    result = []
    while num != 0:
        if num % -2 == 0:
            result.append('0')
            num = num // -2
        else:
            result.append('1')
            num = (num - 1) // -2
    result.reverse()
    print(''.join(result))
