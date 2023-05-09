def main():
    n = int(input())
    sum = 0
    for i in range(1, n):
        sum += i
        if sum >= n:
            print(i)
            break
