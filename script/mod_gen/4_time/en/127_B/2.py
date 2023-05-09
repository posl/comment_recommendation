def algae(r, D, x):
    for i in range(10):
        x = r*x - D
        print(x)
r, D, x = map(int, input().split())
algae(r, D, x)

if __name__ == '__main__':
    algae()