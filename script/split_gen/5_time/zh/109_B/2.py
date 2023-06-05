def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    #print(words)
    flag = True
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            flag = False
            break
        if words.count(words[i]) > 1:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")
