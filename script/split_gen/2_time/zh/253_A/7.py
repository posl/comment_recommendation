def main():
    numbers = input().split()
    numbers = [int(s) for s in numbers]
    numbers.sort()
    if numbers[1] == numbers[0] + numbers[2] - numbers[1]:
        print('是')
    else:
        print('否')
