def are_valid_groups(student_numbers, groups):
    for group in groups:
        if (len(group) == 2 or len(group) == 3) == False:
            return False

    for student in student_numbers:
        occurence = 0
        for group in groups:
            occurence += group.count(student)
        if occurence != 1:
            return False

    return True