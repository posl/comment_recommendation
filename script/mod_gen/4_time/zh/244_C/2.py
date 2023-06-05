def main():
    n = int(input())
    nums = [i for i in range(1, 2*n+2)]
    for i in range(1, 2*n+2):
        print(nums.pop(0))
        flush()
        a = int(input())
        if a == 0:
            break
        nums.remove(a)
        b = nums.pop(-1)
        print(b)
        flush()
        c = int(input())
        if c == 0:
            break
        nums.remove(c)
        nums.insert(0, a)
    exit()

if __name__ == '__main__':
    main()