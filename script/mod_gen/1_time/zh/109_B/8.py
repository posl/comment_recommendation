def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n):
        if i == 0:
            continue
        if words[i][0] != words[i-1][-1]:
            print("No")
            return
        if words.count(words[i]) > 1:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()