def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j == int(i * j ** 0.5) ** 2:
                count += 1
    print(count)
main()
