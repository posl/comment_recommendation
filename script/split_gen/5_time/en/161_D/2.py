def main():
    k = int(input())
    lunlun = [i for i in range(1,10)]
    while len(lunlun) < k:
        new_lunlun = []
        for l in lunlun:
            last_digit = l % 10
            if last_digit == 0:
                new_lunlun.append(l * 10 + last_digit)
                new_lunlun.append(l * 10 + last_digit + 1)
            elif last_digit == 9:
                new_lunlun.append(l * 10 + last_digit - 1)
                new_lunlun.append(l * 10 + last_digit)
            else:
                new_lunlun.append(l * 10 + last_digit - 1)
                new_lunlun.append(l * 10 + last_digit)
                new_lunlun.append(l * 10 + last_digit + 1)
        lunlun = new_lunlun
    print(lunlun[k - 1])
