def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in s:
        if i % 2 == 0:
            if i % 4 != 0:
                count += 1
        else:
            count += 1
    print(count)
