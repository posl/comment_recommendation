def main():
    #get input
    l1,r1,l2,r2 = map(int,input().split())
    #find the length of the part of the line painted both red and blue
    if l2 <= r1 and l1 <= r2:
        answer = min(r1,r2) - max(l1,l2)
    else:
        answer = 0
    #output
    print(answer)

if __name__ == '__main__':
    main()