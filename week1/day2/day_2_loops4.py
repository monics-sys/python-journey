def main():
    x=int(input("Enter the number: "))
    if is_even(x):
        print(f"{x} is even number")
    else:
        print(f"{x} is odd number")

        
def is_even(n):
      if n % 2 == 0:
            return True if n % 2 == 0 else False
main() 