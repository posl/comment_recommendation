def main():
    n = int(input())
    for i in range(0, 26):
        for j in range(0, 16):
            if i*4 + j*7 == n:
                print("Yes")
                return
    print("No")
    return
