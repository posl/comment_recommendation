def get_level(score):
    if score >= 90:
        return "expert"
    elif score >= 70:
        return "high"
    elif score >= 40:
        return "intermediate"
    else:
        return "beginner"

if __name__ == '__main__':
    get_level()