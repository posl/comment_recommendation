def main():
    num = int(input())
    if num == 0:
        print(0)
    else:
        result = ""
        while num != 0:
            if num % 2 == 0:
                result = "0" + result
                num = int(num / (-2))
            else:
                result = "1" + result
                num = int((num - 1) / (-2))
        print(result)
