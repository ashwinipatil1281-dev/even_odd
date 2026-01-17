def check_number(num):
    if num <= 1:
        prime_result = "Not Prime"
    else:
        prime_result = "Prime"
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime_result = "Not Prime"
                break

    if num % 2 == 0:
        even_odd_result = "Even"
    else:
        even_odd_result = "Odd"

    result = (prime_result, even_odd_result)
    return result


