def shiritori(n,words):
    flag = True
    for i in range(1,n):
        if words[i] in words[:i]:
            flag = False
            break
        if words[i][0] != words[i-1][-1]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    shiritori()