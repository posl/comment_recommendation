def run():
    import sys
    args = sys.argv
    if len(args) != 8:
        print("Usage: python problems249_a.py A B C D E F X")
        sys.exit(1)
    A = int(args[1])
    B = int(args[2])
    C = int(args[3])
    D = int(args[4])
    E = int(args[5])
    F = int(args[6])
    X = int(args[7])
    t = 0
    x_h = 0
    x_q = 0
    while True:
        if t >= X:
            break
        x_h += B * A
        x_q += D * E
        t += A + C
        t += D + F
    if x_h > x_q:
        print("高桥")
    elif x_h < x_q:
        print("青木")
    else:
        print("画")

if __name__ == '__main__':
    run()