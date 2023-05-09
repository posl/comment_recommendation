def main():
    min = int(input())
    hh = min // 60
    mm = min % 60
    print('{:02d}:{:02d}'.format(hh + 21, mm))
main()
