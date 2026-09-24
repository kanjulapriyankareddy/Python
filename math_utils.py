



def add(a,b):
    result=a+b
    return result


def sub(a,b):
    result= a-b
    return result

def mul(a,b):
    result=a*b
    return result

def div(a,b):
    if b==0:
        raise ValueError("we cannt divide with zero")
    else:
        result=a/b
        return result