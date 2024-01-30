def calculate_area(length, width):
    if length < 0 or width < 0:
        return "Dimensions must be non-negative values."
    
    if length == width:
        return "This is a square!"
    else:
        area = length * width
        return area

# Program to input values from the user and call the function
def main():
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        
        result = calculate_area(length, width)

        if isinstance(result, str):
            print(result)
        else:
            print(f"The area of the rectangle is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values for length and width.")

if __name__ == "__main__":
    main()
