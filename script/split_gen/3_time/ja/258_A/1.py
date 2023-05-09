def main():
    k = int(input())
    h = 21 + k // 60
    m = k % 60
    print(str(h) + ":" + str(m).zfill(2))
