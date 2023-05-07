def  main():
    s = input()
    l = list(s)
    l.sort()
    count = 1
    for  i  in  range(0, len(l)-1):
        if  l[i] != l[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    ()