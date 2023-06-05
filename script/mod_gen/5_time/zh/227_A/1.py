def last_card(n,k,a):
    if n == 1:
        return 1
    else:
        if k == 1:
            return a
        elif k == 2:
            if a == 1:
                return 2
            else:
                return 1
        else:
            if a == 1:
                return last_card(n,k-1,n)
            else:
                return last_card(n,k-1,a-1)

if __name__ == '__main__':
    last_card()