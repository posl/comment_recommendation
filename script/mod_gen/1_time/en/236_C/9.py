def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    # 1. Create a list of 0s
    # 2. Loop through the list
    # 3. If the station is in the express train list, set the value to 1
    # 4. Print Yes if the value is 1, No if the value is 0
    station_list = [0] * n
    for i in range(n):
        if s[i] in t:
            station_list[i] = 1
    for i in range(n):
        if station_list[i] == 1:
            print("Yes")
        else:
            print("No")
main()

if __name__ == '__main__':
    main()