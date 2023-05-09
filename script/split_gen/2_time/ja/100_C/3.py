def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        while i % 2 == 0:
            count += 1
            i /= 2
    print(count)
