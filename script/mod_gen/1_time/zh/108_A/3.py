def problems108_a():
    k = int(input())
    if k < 2 or k > 100:
        print("输入的k不符合要求")
        return
    count = 0
    for i in range(1, k + 1):
        for j in range(i+1, k + 1):
            if i % 2 == 0 and j % 2 == 1:
                count += 1
    print(count * 2)

if __name__ == '__main__':
    problems108_a()