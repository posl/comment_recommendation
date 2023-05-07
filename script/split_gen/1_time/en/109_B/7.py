def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n):
        if i != 0:
            if words[i] in words[:i]:
                print("No")
                exit()
        if i != n - 1:
            if words[i][-1] != words[i + 1][0]:
                print("No")
                exit()
    print("Yes")
