import sys
import xing_number_validator as xnv

def main():
    exit_commands = ('exit', 'quit', 'q')
    print("Welcome to the Crossing Number Validator!")
    print("Enter a crossing number to validate it.")
    print("Type 'q', 'quit', or 'exit' to exit the application.\n")
    
    while True:
        try:
            xn = input('Enter the crossing number: ').strip()
            if xn.lower() in exit_commands:
                print('Have a safe day!')
                sys.exit()
            
            value = xnv.crossing_number_validation(xn)
            
            if value:
                print("✅ This crossing number is VALID.")
            else:
                print("❌ This crossing number is INVALID.")
            
            print("Please enter another crossing number or type 'q' to quit.\n")
        except KeyboardInterrupt:
            print('\nOperation cancelled by user. Have a safe day!')
            sys.exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again or type 'q' to quit.\n")

if __name__ == "__main__":
    main()
