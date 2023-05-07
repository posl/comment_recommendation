def solve():
    s = input()
    if len(s) == 1:
        print("Yes" if s == "8" else "No")
        return
    if len(s) == 2:
        print("Yes" if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0 else "No")
        return
    counts = [0] * 10
    for c in s:
        counts[int(c)] += 1
    for i in range(112, 1000, 8):
        if not is_valid(i, counts):
            continue
        print("Yes")
        return
    print("No")
