def main():
    a = raw_input().split()
    b = [0]*10
    for i in range(10):
        b[i] = int(a[i])
    for j in range(3):
        b[0] = b[b[0]]
    print b[0]
