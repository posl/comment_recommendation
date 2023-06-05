def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    if len(set(words)) == len(words):
        for i in range(1,n):
            if words[i][0] != words[i-1][-1]:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")
