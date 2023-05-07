def main():
    S = input()
    tmp = []
    for i in S:
        if i not in tmp:
            tmp.append(i)
        else:
            tmp.remove(i)
    if len(tmp) == 0:
        print(-1)
    else:
        print(tmp[0])
