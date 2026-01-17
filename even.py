def even_odd(n):
    if n <= 1:
        prime_status = "Not Prime"
    else:
        prime_status = "Prime"
        for i in range(2, n):
            if n % i == 0:
                prime_status = "Not Prime"
                break
            if n % 2 == 0:
              even_odd = "Even"
            else:
              even_odd = "Odd"
    return prime_status, even_odd
  
