def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in A:
        if i > 10:
            count += i - 10
    print(count)
