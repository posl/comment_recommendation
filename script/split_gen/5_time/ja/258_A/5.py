def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print(str(21+h).zfill(2) + ":" + str(m).zfill(2))
