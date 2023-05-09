def main():
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    for i in range(1, N):
        if words[i - 1][-1] != words[i][0]:
            print("No")
            return
        else:
            if words[i] in words[:i]:
                print("No")
                return
    print("Yes")
