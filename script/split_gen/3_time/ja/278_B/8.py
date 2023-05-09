def main():
    h,m = map(int, input().split())
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    print(f"{h:02} {m:02}")
