number = int(input("Enter an integer: "))
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

  number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")