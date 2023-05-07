def solve(W,H,x,y):
    if W == x and H == y:
        return (W*H)/2, 1
    elif W == x or H == y:
        return (W*H)/2, 0
    else:
        return (W*H)/2, 0

if __name__ == '__main__':
    solve()