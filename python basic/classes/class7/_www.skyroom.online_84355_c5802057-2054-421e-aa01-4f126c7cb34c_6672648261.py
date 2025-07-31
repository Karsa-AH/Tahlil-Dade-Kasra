def salary(exp, job, edu = 'ms', base_slary = 12500000):
    salary = base_slary
    salary = salary + 0.2 * exp * salary
    if job == 1:
        salary += 0.2 * salary
    match edu:
        case "phd":
            salary += 0.3 * salary
        case "ms":
            salary += 0.2 * salary
        case "bc":
            salary += 0.1 * salary
        # case _:
        # pass
    """
    if edu == 'php':
        salary += .3 * salary
    elif edu == 'ms':
        salary += .2 * salary'
    """
    return salary


print("18,1,'ms',12500000: ", salary(exp = 18, job = 1, base_slary = 20000000, edu = "ms"))
print("5,0,'bc',12500000: ", salary(5, 0, "bc"))
a =  salary(18, 1, "ms")
b = salary(5, 0, "bc")
