def main():
    s = input()
    count = 0
    for i in range(10000):
        if len(str(i)) < 4:
            if s.count("o") > 0:
                count = 0
                break
            else:
                count += 1
        else:
            if s.count(str(i)) == 4:
                count += 1
    print(count)
