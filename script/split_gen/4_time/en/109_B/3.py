def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    if len(words) != len(set(words)):
        print("No")
        return
    for i in range(1, n):
        if words[i][0] != words[i - 1][-1]:
            print("No")
            return
    print("Yes")
