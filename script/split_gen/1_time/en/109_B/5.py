def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print('No')
            return
        if i != 0 and words[i-1][-1] != word[0]:
            print('No')
            return
        words.append(word)
    print('Yes')
