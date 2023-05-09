def main():
    s = input()
    count = 0
    for i in range(10000):
        pin = str(i).zfill(4)
        for j in range(10):
            if s[j] == 'o' and str(j) not in pin:
                break
            if s[j] == 'x' and str(j) in pin:
                break
        else:
            count += 1
    print(count)
