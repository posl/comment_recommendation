def main():
    k = int(input())
    if k < 2 or k > 100:
        return
    count = 0
    for i in range(1, k + 1, 2):
        for j in range(2, k + 1, 2):
            count += 1
    print(count)
main()
