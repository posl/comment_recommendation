def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            continue
        else:
            factor_list = []
            for j in range(1, i + 1):
                if i % j == 0:
                    factor_list.append(j)
            if len(factor_list) == 8:
                count += 1
    print(count)
