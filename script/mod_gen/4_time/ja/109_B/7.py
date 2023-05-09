def main():
    n = int(input())
    word = []
    for i in range(n):
        word.append(input())
    flag = True
    for i in range(n):
        for j in range(i+1,n):
            if word[i] == word[j]:
                flag = False
            if word[i][-1] != word[j][0]:
                flag = False
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()