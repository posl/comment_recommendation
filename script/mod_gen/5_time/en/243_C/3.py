def main():
    n = int(input())
    people = []
    for i in range(n):
        people.append(list(map(int, input().split())))
    s = input()
    for i in range(n):
        if s[i] == 'L':
            people[i][0] *= -1
    people.sort(key=lambda x: x[0])
    for i in range(n-1):
        if people[i][0] < 0 and people[i+1][0] > 0:
            if people[i][1] >= people[i+1][1]:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()