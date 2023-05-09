def solve(N):
    if len(N) == 2:
        return int(N[0])*int(N[1])
    if len(N) == 3:
        return int(N[0])*int(N[1])*int(N[2])
    if len(N) == 4:
        return max(int(N[0])*int(N[1])*int(N[2]), int(N[0])*int(N[1])*int(N[3]), int(N[0])*int(N[2])*int(N[3]), int(N[1])*int(N[2])*int(N[3]))
    if len(N) == 5:
        return max(int(N[0])*int(N[1])*int(N[2])*int(N[3]), int(N[0])*int(N[1])*int(N[2])*int(N[4]), int(N[0])*int(N[1])*int(N[3])*int(N[4]), int(N[0])*int(N[2])*int(N[3])*int(N[4]), int(N[1])*int(N[2])*int(N[3])*int(N[4]))
    if len(N) == 6:
        return max(int(N[0])*int(N[1])*int(N[2])*int(N[3])*int(N[4]), int(N[0])*int(N[1])*int(N[2])*int(N[3])*int(N[5]), int(N[0])*int(N[1])*int(N[2])*int(N[4])*int(N[5]), int(N[0])*int(N[1])*int(N[3])*int(N[4])*int(N[5]), int(N[0])*int(N[2])*int(N[3])*int(N[4])*int(N[5]), int(N[1])*int(N[2])*int(N[3])*int(N[4])*int(N[5]))
    if len(N) == 7:
        return max(int(N[0])*int(N[1])*int(N[2])*int(N[3])*int(N[4])*int(N[5]), int(N[0])*int(N[1])*int(N[2])*int(N[3])*int(N[4])*int(N[6]), int(N[0])*int(N[1])*int(N[2])*int(N[3])*int(N[5])*int(N[6]), int(N

if __name__ == '__main__':
    solve()