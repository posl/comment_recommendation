def solve():
    s = [input() for _ in range(4)]
    if "H" in s and "2B" in s and "3B" in s and "HR" in s:
        print("Yes")
    else:
        print("No")
