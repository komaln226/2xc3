def are_valid_groups(student_numbers, groups):
    if not all(len(x) == 2 or len(x) == 3 for x in groups):
        return False

    for student in student_numbers:
        occ = 0
        for group in groups:
            occ += group.count(student)
        if occ != 1:
            return False

    return True
