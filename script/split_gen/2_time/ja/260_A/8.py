def main():
    s = input()
    l = list(s)
    l2 = []
    for i in l:
        if i in l2:
            continue
        else:
            l2.append(i)
    if len(l) == len(l2):
        print("-1")
    else:
        for i in l2:
            if l.count(i) == 1:
                print(i)
                break
