def main():
    k = int(input())
    print("".join([chr(ord('A') + i) for i in range(k)]))
