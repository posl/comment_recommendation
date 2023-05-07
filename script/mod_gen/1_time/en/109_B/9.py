def main():
    n = input()
    words = []
    for i in range(int(n)):
        words.append(input())
    result = 'Yes'
    for i in range(len(words)):
        if i == 0:
            continue
        if words[i] in words[:i]:
            result = 'No'
            break
        if words[i][0] != words[i-1][-1]:
            result = 'No'
            break
    print(result)

if __name__ == '__main__':
    main()