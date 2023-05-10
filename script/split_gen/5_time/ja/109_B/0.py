def check(w, words):
    if w in words:
        return False
    if len(words) == 0:
        return True
    if w[0] != words[-1][-1]:
        return False
    return True
n = int(input())
words = []
for i in range(n):
    w = input()
    if not check(w, words):
        print('No')
        exit()
    words.append(w)
print('Yes')
