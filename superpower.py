def ifWholeNum(x):
    temp = int(x)
    if abs(x-temp) == 0:
        return True
    return False

test = 1
while test < 2**64:
    count = 0
    power = 2
    while count < 2 and power < 64:
        #     ifInteger( test ** (1./ power) ) check if test^(1/n) is a whole number  thus test^n exists
        if ifWholeNum( test ** (1./ power) ):
            count += 1
        power += 1
    if count == 2:
        print str(test)
    test +=1


# power = 0
# check if int(test ** (1./test)) % 10 == 0

# test = 1, count = 0, power=2
