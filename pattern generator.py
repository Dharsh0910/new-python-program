def generate_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print((str(i) + " ") * i)

def verify_pattern(rows):
    for i in range(1, rows + 1):
        expected_pattern = " " * (rows - i) + (str(i) + " ") * i
        generated_pattern = " " * (rows - i) + (str(i) + " ") * i
        if generated_pattern != expected_pattern:
            return False
    return True

def main():
    rows = int(input("Enter the number of rows for the pattern: "))
    
    print("\nGenerated Pattern:")
    generate_pattern(rows)
    
    if verify_pattern(rows):
        print("\nPattern verified correctly.")
    else:
        print("\nPattern verification failed.")

if __name__ == "__main__":
    main()

