def main():
    hw = input()
    hw = hw.split()
    h = int(hw[0])
    w = int(hw[1])
    hw = input()
    hw = hw.split()
    hh = int(hw[0])
    ww = int(hw[1])
    print((h-hh)*(w-ww))
    return 0
