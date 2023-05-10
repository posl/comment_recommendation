def main():
    h,w,n = map(int,input().split())
    card = {}
    for i in range(1,n+1):
        a,b = map(int,input().split())
        card[i] = [a,b]
    #print(card)
    rows = {}
    cols = {}
    for i in range(1,h+1):
        rows[i] = 0
    for i in range(1,w+1):
        cols[i] = 0
    for i in range(1,n+1):
        rows[card[i][0]] += 1
        cols[card[i][1]] += 1
    #print(rows)
    #print(cols)
    #print(sorted(rows.items(), key=lambda x:x[1]))
    #print(sorted(cols.items(), key=lambda x:x[1]))
    for i in range(1,h+1):
        if rows[i] == 0:
            del rows[i]
    for i in range(1,w+1):
        if cols[i] == 0:
            del cols[i]
    #print(rows)
    #print(cols)
    rows = sorted(rows.items(), key=lambda x:x[1])
    cols = sorted(cols.items(), key=lambda x:x[1])
    #print(rows)
    #print(cols)
    #print(rows[0][0])
    #print(cols[0][0])
    #print(rows[0][1])
    #print(cols[0][1])
    for i in range(1,n+1):
        if rows[0][1] < cols[0][1]:
            print(rows[0][0],card[i][1])
            rows[0] = (rows[0][0],rows[0][1]+1)
        else:
            print(card[i][0],cols[0][0])
            cols[0] = (cols[0][0],cols[0][1]+1)

if __name__ == '__main__':
    main()