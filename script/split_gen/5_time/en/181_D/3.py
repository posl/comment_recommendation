def main():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("Yes")
            return
        else:
            print("No")
            return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("Yes")
            return
        else:
            print("No")
            return
    count = [0 for _ in range(10)]
    for i in s:
        count[int(i)] += 1
    for i in range(112, 1000, 8):
        tmp = [0 for _ in range(10)]
        tmp[1] += 1
        tmp[1] += count[1]
        tmp[1] += count[1]
        tmp[2] += 1
        tmp[2] += count[2]
        tmp[2] += count[2]
        tmp[2] += count[2]
        tmp[3] += 1
        tmp[3] += count[3]
        tmp[3] += count[3]
        tmp[3] += count[3]
        tmp[4] += 1
        tmp[4] += count[4]
        tmp[4] += count[4]
        tmp[4] += count[4]
        tmp[5] += 1
        tmp[5] += count[5]
        tmp[5] += count[5]
        tmp[5] += count[5]
        tmp[6] += 1
        tmp[6] += count[6]
        tmp[6] += count[6]
        tmp[6] += count[6]
        tmp[7] += 1
        tmp[7] += count[7]
        tmp[7] += count[7]
        tmp[7] += count[7]
        tmp[8] += 1
        tmp[8] += count[8]
        tmp[8] += count[8]
        tmp[8] += count[8]
        tmp[9] += 1
        tmp[9] += count[9]
        tmp[9] += count[9]
        tmp[9] += count[9]
        if tmp[0] == 0 and tmp
