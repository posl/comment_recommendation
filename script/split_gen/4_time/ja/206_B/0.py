def main():
    n = int(input())
    sum = 0
    i = 0
    while True:
        i += 1
        sum += i
        if sum >= n:
            break
    print(i)
