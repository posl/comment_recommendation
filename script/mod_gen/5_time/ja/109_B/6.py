def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print('No')
            return
        else:
            words.append(word)
        if i > 0:
            if word[0] != words[i-1][-1]:
                print('No')
                return
    print('Yes')
main()
