def main():
    h,w,n = map(int,input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int,input().split())))
    for i in range(n):
        cards[i].append(i+1)
    cards.sort(key=lambda x:x[0])
    cards.sort(key=lambda x:x[1])
    for i in range(n):
        print(cards[i][2],cards[i][0],cards[i][1])

if __name__ == '__main__':
    main()