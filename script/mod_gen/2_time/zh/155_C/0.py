def main():
    n = int(input())
    dic = {}
    for i in range(n):
        word = input()
        dic[word] = dic.get(word, 0) + 1
    max = 0
    for key in dic:
        if max < dic[key]:
            max = dic[key]
    for key in sorted(dic):
        if dic[key] == max:
            print(key)
main()
