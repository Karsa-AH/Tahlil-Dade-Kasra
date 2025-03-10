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
salary1 =  salary(18, 1, "ms")



def tax(salary=salary1,basetax=1000):                           
    a=basetax
    if(salary>15000000):
        return a + (0.1*basetax)
tax1=tax()  


def insu(salary=salary1,base=1000):
    a=salary
    return a*0.7
insu1 = insu()


def net_salary(salary=salary1,tax=tax1,insu=insu1):
    return salary-(tax+insu)

if __name__ == "__main__":
    print(salary(18, 1, "ms"),net_salary(),tax(),insu())
#ths if will execute when we run this file / but if we use it with import it wont execute
