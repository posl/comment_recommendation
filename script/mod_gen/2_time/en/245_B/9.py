def find_missing_number(numbers):
    numbers.sort()
    if numbers[0] != 0:
        return 0
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] > 1:
            return numbers[i - 1] + 1
    return numbers[-1] + 1
n = int(input())
numbers = list(map(int, input().split()))
print(find_missing_number(numbers))

if __name__ == '__main__':
    find_missing_number()