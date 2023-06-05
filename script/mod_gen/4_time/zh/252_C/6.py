def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    min = 1000000000
    for i in range(n):
        count = 0
        for j in range(n):
            if i == j:
                continue
            else:
                if s[j].find(s[i]) == -1:
                    count += 1
        if count < min:
            min = count
    if min == 1000000000:
        print(10)
    else:
        print(min)
    return 0

if __name__ == '__main__':
    main()