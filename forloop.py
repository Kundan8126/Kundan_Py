def array(*numbers):
    total = sum(numbers)
    return total

choice = int(input("Enter a choice between: \n1. HEY\n2. HELLO\n"))

if choice == 1:
    for i in range(10):
        print("hey")
elif choice == 2:
    for i in range(10):
        print("hello")
else:
    print("You should've entered a valid choice. Since you chose another option, here is the sum of the first 5 numbers:")
    result = array(1, 2, 3, 4, 5)
    print("Sum:", result,type(result)) 
print("HAVE A GOOD DAY...KEEP SMILING")
