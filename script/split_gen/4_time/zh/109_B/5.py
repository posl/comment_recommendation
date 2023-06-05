def check_shiritori(words):
    for i in range(len(words)):
        if i == 0:
            continue
        if words[i][0] != words[i-1][-1]:
            return False
    return True
n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)
