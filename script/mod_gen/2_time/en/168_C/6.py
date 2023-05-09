def main():
    A, B, H, M = map(int, input().split())
    # The hour hand rotates 360 degrees in 12 hours, so it rotates 30 degrees in 1 hour.
    # The minute hand rotates 360 degrees in 60 minutes, so it rotates 6 degrees in 1 minute.
    # The hour hand rotates 30 degrees in 60 minutes, so it rotates 0.5 degrees in 1 minute.
    # The minute hand rotates 6 degrees in 1 hour, so it rotates 0.1 degrees in 1 minute.
    # So, the hour hand rotates 0.5 degrees in 1 minute and the minute hand rotates 0.1 degrees in 1 minute.
    # The hour hand rotates 30 degrees in 1 hour and the minute hand rotates 6 degrees in 1 hour.
    # So, the hour hand rotates 0.5 degrees in 1 hour and the minute hand rotates 0.1 degrees in 1 hour.
    # The hour hand rotates 360 degrees in 12 hours and the minute hand rotates 360 degrees in 60 minutes.
    # So, the hour hand rotates 0.5 degrees in 12 hours and the minute hand rotates 0.1 degrees in 60 minutes.
    # The hour hand rotates 30 degrees in 1 hour and the minute hand rotates 6 degrees in 1 minute.
    # So, the hour hand rotates 0.5 degrees in 1 minute and the minute hand rotates 0.1 degrees in 1 minute.
    # The hour hand rotates 0.5 degrees in 1 minute and the minute hand rotates 0.1 degrees in 1 minute.
    # The hour hand rotates 0.5 degrees in 1 hour and the minute hand rotates 0.1 degrees in 1 hour.
    # The hour hand rotates 0.5 degrees in 12 hours and the minute hand rotates 0.1 degrees in 60 minutes.
    # The hour hand rotates 0.5 degrees in 1 minute and the minute hand rotates 0.1 degrees in 1 minute.
    # The hour hand rotates 0.5 degrees in 1 hour and the minute hand rotates 0.1 degrees in 1 hour.
    # The hour hand rotates 0.5 degrees in 12 hours and the minute hand rotates 0

if __name__ == '__main__':
    main()