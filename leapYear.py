#empty method for now

def leapYear(a):
    if ( a % 400 == 0 ):
        return True
    if ( a % 100 == 0 ):
        return False
    if ( a % 4 == 0 ):
        return True
    return False
