def main():
    n = int(input())
    count = 0
    while True:
        flag = False
        for i in range(2, n):
            if n % i == 0:
                flag = True
                n = n // i
                count += 1
                break
        if not flag:
            break
    print(count)
