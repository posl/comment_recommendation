def main():
    #N = int(input())
    N = 100000
    count = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            count += 1
        elif i % 10 == 1:
            count += 1
        elif i % 100 == 1:
            count += 1
        elif i % 1000 == 1:
            count += 1
        elif i % 10000 == 1:
            count += 1
        elif i % 100000 == 1:
            count += 1
    print(count)
