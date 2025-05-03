def get_grade(s1, s2, s3):
    GRADES = {
        "A": (90, 100),
        "B": (80, 90),
        "C": (70, 80),
        "D": (60, 70),
        "F": (0, 60)
    }
    average = (s1 + s2 + s3) / 3
    for grade, (low, high) in GRADES.items():
        if low <= average <= high:
            return grade
