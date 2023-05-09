def main():
    numbers = [int(x) for x in input().split()]
    for i in range(len(numbers)):
        if numbers[i] == 0:
            print(i+1)
            break
