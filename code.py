def are_valid_groups(students, groups):
    
    def inGroups(student, groups):
        occurence = 0
        for i in range(0, len(groups)):
            for j in range(0, len(groups[0])):
                if student == groups[i][j]:
                    occurence += 1
                if occurence > 1:
                    return False
        if occurence == 1:
            return True
        return False
    
    for student in students:
        if inGroups(student, groups) == False:
            return False
    return True