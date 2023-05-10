def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    cx = []
    cy = []
    cr = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        cx.append(x)
        cy.append(y)
        cr.append(r)
    #print(N, sx, sy, tx, ty)
    #print(cx, cy, cr)
    #print('------------------')
    #print('------------------')

if __name__ == '__main__':
    main()