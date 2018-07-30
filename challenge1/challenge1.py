
def allEvenDigits(start_num, end_num):
    """
    This function returns the numbers with all even digits between
    start_num and end_num inclusive.
    """
    result = []
    for num in range(start_num, end_num+1):
        allEven = True
        # check to see if the digits are all even
        for digit in str(num):
            if int(digit) % 2 != 0:
                allEven = False
                break
        if allEven:
            result.append(num)
    return result

if __name__ == '__main__':
    result = allEvenDigits(1000, 3000)
    # print returned result as a string
    for i in range(len(result)):
        if i != len(result)-1:
            print(str(result[i])+","),
        else:
            print(str(result[i]))
