def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(len(words)):
        if i == 0:
            continue
        if words[i] in words[:i]:
            print("No")
            return
        if words[i][0] != words[i-1][-1]:
            print("No")
            return
    print("Yes")
