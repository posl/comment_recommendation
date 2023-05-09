def check(word, words):
    if word in words:
        return False
    if len(words) == 0:
        return True
    if words[-1][-1] != word[0]:
        return False
    return True
n = int(input())
words = []
for i in range(n):
    word = input()
    if not check(word, words):
        print("No")
        exit()
    words.append(word)
print("Yes")

if __name__ == '__main__':
    check()