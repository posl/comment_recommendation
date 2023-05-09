def main():
    k = int(input())
    print('22:03' if k>63 else '21:45' if k>45 else '21:40' if k>40 else '21:30' if k>30 else '21:15' if k>15 else '21:00')

if __name__ == '__main__':
    main()