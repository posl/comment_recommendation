def run():
    a, b, c, d, e, f, x = map(int, input().split())
    t = 0
    while True:
        if t % (a + b) < a:
            x -= e
        t += 1
        if x <= 0:
            print("Takahashi")
            break

if __name__ == '__main__':
    run()