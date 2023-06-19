def snuke(k):
    result = []
    for i in range(1, 10):
        result.append(i)
    count = 9
    while count < k:
        for i in range(len(result)):
            for j in range(10):
                n = result[i] * 10 + j
                if n % (sum(map(int, str(n)))) == 0:
                    result.append(n)
                    count += 1
                    if count == k:
                        return result
    return result
k = int(input())
result = snuke(k)
for i in range(k):
    print(result[i])
