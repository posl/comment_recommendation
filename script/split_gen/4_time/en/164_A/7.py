def sheep_and_wolves():
    sheep, wolves = map(int, input().split())
    if sheep <= wolves:
        print("unsafe")
    else:
        print("safe")
