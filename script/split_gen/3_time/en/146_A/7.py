def main():
    # Write your code here
    s = input()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(days.index("SUN") - days.index(s) + 7)
