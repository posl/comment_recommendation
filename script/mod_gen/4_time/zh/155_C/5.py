def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    words.sort()
    max_count = 0
    max_words = []
    count = 1
    for i in range(1, n):
        if words[i] == words[i - 1]:
            count += 1

if __name__ == '__main__':
    main()