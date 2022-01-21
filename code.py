def are_valid_group(studentNumber, groups):
    result = False
    for x in studentNumber:
        for y in groups:
            if x == y:
                result = True 
                return result