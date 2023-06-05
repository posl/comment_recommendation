def count_vw(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "v":
            for j in range(i+1, len(s)):
                if s[j] == "w":
                    count += 1
                else:
                    break
    return count

if __name__ == '__main__':
    count_vw()