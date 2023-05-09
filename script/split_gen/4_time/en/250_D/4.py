def main():
    N = int(input())
    count = 0
    for i in range(2, 10 ** 6):
        if i ** 3 > N:
            break
        for j in range(i + 1, 10 ** 6):
            if i * j ** 3 > N:
                break
            count += 1
    print(count)
