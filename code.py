def are_valid_groups(student_numbers, groups):
    for student in student_numbers:
        if (not any(student in x for x in groups)):
            return False
    return True
