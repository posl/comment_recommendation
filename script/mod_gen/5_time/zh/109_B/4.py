def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n):
        for j in range(i+1,n):
            if words[i] == words[j]:
                print('No')
                return
    for i in range(1,n):
        if words[i][0] != words[i-1][-1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()