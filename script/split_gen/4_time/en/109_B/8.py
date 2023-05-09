def main():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    if len(set(words)) == len(words):
        if len(set([w[0] for w in words])) == len(words):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
