def main():
    k = int(input())
    s = input()
    t = input()
    card = [k]*9
    for i in range(4):
        card[int(s[i])-1] -= 1
        card[int(t[i])-1] -= 1
    total = 9*k-8
    win = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j and card[i-1] < 2:
                continue
            if i != j and card[i-1] < 1 or card[j-1] < 1:
                continue
            if i == j:
                win += card[i-1]*(card[i-1]-1)
            else:
                win += card[i-1]*card[j-1]
    print(win/total/(total-1))

if __name__ == '__main__':
    main()