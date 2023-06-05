def main():
    N = int(input())
    word_list = []
    word_list.append(input())
    for i in range(N-1):
        word_list.append(input())
    for i in range(N-1):
        if word_list[i][-1] != word_list[i+1][0]:
            print('No')
            exit()
        for j in range(i+1,N):
            if word_list[i] == word_list[j]:
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()