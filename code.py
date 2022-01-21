def are_valid_groups(student_numbers, groups):
    if not any((2 > len(x) > 3) for x in groups):
        return False

    for student in student_numbers:
        occ = 0
        for group in groups:
            occ += group.count(student)
        if 0 < occ < 2:
            return False

    return True
