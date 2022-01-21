def are_valid_groups(student_numbers, groups):
    for studentid in student_numbers:
        if not any(student in x groups):
            return True
        else:
            return False