def find_rgb(s):
    rgb = []
    for i in range(len(s)):
        if s[i] == 'R':
            rgb.append([i, 0])
        elif s[i] == 'G':
            rgb.append([i, 1])
        else:
            rgb.append([i, 2])
    return rgb

if __name__ == '__main__':
    find_rgb()