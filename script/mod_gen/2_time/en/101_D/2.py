def snuke():
    K = int(input())
    snuke_numbers = [1]
    for i in range(K):
        print(snuke_numbers[i])
        snuke_numbers.append(snuke_numbers[i] * 10)
        snuke_numbers.append(snuke_numbers[i] * 10 + 1)
        snuke_numbers.sort()

if __name__ == '__main__':
    snuke()