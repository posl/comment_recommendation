def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        count += is_seven_five(i)
    print(count)
