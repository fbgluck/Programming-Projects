# prime_number_calculator using functions   
def calculate_primes(low,high):
    target = low
    for i in range (2,high):
        if target%i == 0:
            print (f"The result of {target}/{i} is {target/i} so the number has a divisor other thatn itself and 1")
        else:
            target = target +1;    


calculate_primes(4,5)
