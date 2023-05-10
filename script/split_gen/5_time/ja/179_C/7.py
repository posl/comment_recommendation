def main():
    N = int(input())
    count = 0
    for i in range(1,N):
        tmp = N - i
        for j in range(1,tmp):
            if tmp % j == 0:
                count += 1
    print(count)
