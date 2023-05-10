def main():
    n = input()
    p = [int(x) for x in input().split()]
    min = p[0]
    count = 1
    for i in range(1, int(n)):
        if p[i] <= min:
            count += 1
            min = p[i]
    print(count)
