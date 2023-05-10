def can_buy_all(N, X, A):
    if sum(A) - (len(A) / 2) <= X:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    can_buy_all()