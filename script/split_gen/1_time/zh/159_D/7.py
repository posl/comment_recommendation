def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    count = {}
    for i in A:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    total = 0
    for i in count.values():
        total += i * (i - 1) // 2
    for i in A:
        print(total - (count[i] - 1))
