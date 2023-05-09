def solve(H,M):
    if H==0:
        H=24
    if M==0:
        M=60
    while True:
        M-=1
        if M==-1:
            M=59
            H-=1
        if H==-1:
            H=23
        if H==24:
            H=0
        if isConfusing(H,M):
            return H,M

if __name__ == '__main__':
    solve()