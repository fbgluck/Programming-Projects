# prime_number_calculator using functions
# A prime number is divisible only by itself and 1
# or -- one number in the range of 2 through target-1 is evenly divisible   
def calculate_primes(low,high):
    target = low
    print(f"Testing from {low} to {high}")
    for i in range (2,high-1):
        for j in range (2,i) and goAgain:
            if target%j == 0: # if true, number is evenly divisible
                print(f"{target} is not prime.")
                goAgain = False
                #print (f"The result of {target}/{j} is {target/j} so the number has a divisor other thatn itself and 1")
        else:
            target = target +1;    


calculate_primes(4,9)
