def main():
    a = [int(x) for x in input().split()]
    b = [chr(x+96) for x in a]
    print("".join(b))
main()
