def main():
    n, k = map(int, input().split())
    people = []
    for i in range(n):
        a, b = map(int, input().split())
        people.append([a, b])
    people.sort()
    i = 0
    while k > 0 and i < n:
        if k >= people[i][0]:
            k += people[i][1]
        else:
            break
        i += 1
    print(k)

if __name__ == '__main__':
    main()