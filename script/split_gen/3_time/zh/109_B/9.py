def shiritori(n, words):
    if len(words) != len(set(words)):
        return False
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            return False
    return True
n = int(input())
words = [input() for _ in range(n)]
