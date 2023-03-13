def aboveBelow(lst, comparisonValue):
    countAbove = 0
    countBelow = 0
    
    for num in lst:
        if num > comparisonValue:
            countAbove += 1
        elif num < comparisonValue:
            countBelow += 1
            
    result = {'above': countAbove, 'below': countBelow}
    
    return result

def stringRotation(originalString, rotationAmount):
    effectiveRotation = rotationAmount % len(originalString)
    rotatedString = originalString[-effectiveRotation:] + originalString[:-effectiveRotation]
    return rotatedString

myList = [1, 5, 2, 1, 10]
comparisonValue = 6
result = aboveBelow(myList, comparisonValue)
print("Above count: {}".format(result['above']))
print("Below count: {}".format(result['below']))

originalString = 'MyString'
rotationAmount = 2
rotatedString = stringRotation(originalString, rotationAmount)
print(rotatedString)