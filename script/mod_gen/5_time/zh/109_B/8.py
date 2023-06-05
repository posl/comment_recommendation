def problem109b():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(1,n):
        if words[i-1][-1] != words[i][0]:
            print("No")
            return
    if len(set(words)) == n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problem109b()