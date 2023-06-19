def main():
    num = int(input())
    number = input().split()
    sum = 0
    for i in range(num):
        sum += int(number[i])
    print(sum)
