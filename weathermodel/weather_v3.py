def weathermodel(filename):
    print("Weather Model: Reading from file")

    try:
        with open(filename, "r") as file:
            print(f"{'a':<8} {'b':<8} {'time':<8} {'temp':<10}")
            print("-" * 40)

            for line in file:
                parts = line.strip().split(",")

                if len(parts) == 4:
                    a = float(parts[0])
                    b = float(parts[1])
                    c = float(parts[2])
                    time_x = float(parts[3])

                    temp = (a * (time_x ** 2)) + (b * time_x) + c

                    print(f"{a:<8.2f} {b:<8.2f} {time_x:<8.2f} {temp:<10.2f}")

    except FileNotFoundError:
        print("The file was not found.")


weathermodel("weather_data.txt")