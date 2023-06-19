def func(N):
    N = str(N)
    n = len(N)
    if n == 2:
        return int(N[0])*int(N[1])
    elif n == 3:
        return max(int(N[0])*int(N[1])*int(N[2]), int(N[0])*int(N[1]+N[2]), int(N[0]+N[1])*int(N[2]))
    elif n == 4:
        return max(int(N[0])*int(N[1])*int(N[2])*int(N[3]), int(N[0])*int(N[1])*int(N[2]+N[3]), int(N[0])*int(N[1]+N[2])*int(N[3]), int(N[0]+N[1])*int(N[2])*int(N[3]), int(N[0])*int(N[1]+N[2]+N[3]), int(N[0]+N[1])*int(N[2]+N[3]), int(N[0]+N[1]+N[2])*int(N[3]))
    elif n == 5:
        return max(int(N[0])*int(N[1])*int(N[2])*int(N[3])*int(N[4]), int(N[0])*int(N[1])*int(N[2])*int(N[3]+N[4]), int(N[0])*int(N[1])*int(N[2]+N[3])*int(N[4]), int(N[0])*int(N[1]+N[2])*int(N[3])*int(N[4]), int(N[0]+N[1])*int(N[2])*int(N[3])*int(N[4]), int(N[0])*int(N[1])*int(N[2]+N[3]+N[4]), int(N[0])*int(N[1]+N[2]+N[3])*int(N[4]), int(N[0]+N[1])*int(N[2])*int(N[3]+N[4]), int(N[0])*int(N[1]+N[2]+N[3]+N[4]), int(N[0]+N[1])*int(N[2]+N[3])*int(N[4]), int(N[0]+N[1]+N[2])*int(N[3])*int(N[4]), int(N[0

if __name__ == '__main__':
    func()