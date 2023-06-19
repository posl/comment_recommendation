def solve(n,m,k):
    if n == 1:
        return k
    if n == 2:
        return int((k+1)*k/2)
    if n == 3:
        return int((k+1)*k/2*(k+2)/3)
    if n == 4:
        return int((k+1)*k/2*(k+2)/3*(k+3)/4)
    if n == 5:
        return int((k+1)*k/2*(k+2)/3*(k+3)/4*(k+4)/5)
    if n == 6:
        return int((k+1)*k/2*(k+2)/3*(k+3)/4*(k+4)/5*(k+5)/6)
    if n == 7:
        return int((k+1)*k/2*(k+2)/3*(k+3)/4*(k+4)/5*(k+5)/6*(k+6)/7)
    if n == 8:
        return int((k+1)*k/2*(k+2)/3*(k+3)/4*(k+4)/5*(k+5)/6*(k+6)/7*(k+7)/8)
    if n == 9:
        return int((k+1)*k/2*(k+2)/3*(k+3)/4*(k+4)/5*(k+5)/6*(k+6)/7*(k+7)/8*(k+8)/9)
    if n == 10:
        return int((k+1)*k/2*(k+2)/3*(k+3)/4*(k+4)/5*(k+5)/6*(k+6)/7*(k+7)/8*(k+8)/9*(k+9)/10)
    if n == 11:
        return int((k+1)*k/2*(k+2)/3*(k+3)/4*(k+4)/5*(k+5)/6*(k+6)/7*(k+7)/8*(k+8)/9*(k+9)/10*(k+10)/11)
    if n == 12:
        return int((k+1)*k/2*(k+2)/3

if __name__ == '__main__':
    solve()