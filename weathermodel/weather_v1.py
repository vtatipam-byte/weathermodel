def weathermodel():
    print("weather model:Hard-coded")
    a=0.5
    b=2.5
    c=10.0
    time_x=5.0
    temp=(a*(time_x**2))+(b*time_x)+c 
    print(f"At time {time_x},the predicted temperature is {temp}")

weathermodel()