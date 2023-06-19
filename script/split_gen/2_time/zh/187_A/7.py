def main():
    num1, num2 = map(int, input().split())
    sum1 = sum([int(i) for i in str(num1)])
    sum2 = sum([int(i) for i in str(num2)])
    if sum1 >= sum2:
        print(sum1)
    else:
        print(sum2)
