def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

while True:
    print("\n===== SIMPLE CALCULATION=====")
    print("1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Exit")
    
    choice = input("Enter choice: ")
    if choice == '5':
        print("Exiting calculator...")
        break

    # >>> MOVED INSIDE WHILE LOOP <<<
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(a,b))
    elif choice == '2':
        print("Result:", sub(a,b))
    elif choice == '3':
        print("Result:", mul(a,b))
    elif choice == '4':
        print("Result:", div(a,b))
    else:
        print("Invalid Option!")
