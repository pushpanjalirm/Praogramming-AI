def compare_numbers(num1, num2):
    if num1 > num2:
        return "greater"
    elif num1 == num2:
        return "equal"
    else:
        return "less"
print(compare_numbers(10, 5)) ;
print(compare_numbers(5, 5)) ;
print(compare_numbers(12, 7)) ;
