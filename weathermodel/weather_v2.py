def weathermodel():
    print("Weather Model: Keyboard Input")
    
    try:
        a= float(input("Enter coefficient a: "))
        b= float(input("Enter coefficient b: ")) 
        c= float(input("Enter coefficient c: "))
        time = float(input("Enter time(x): "))

        temp= (a* (time**2)) + (b*time) + c 
        print(f"At time (time) the predicted temperature is {temp}")
    except ValueError:
        print("Invalid input")
weathermodel()