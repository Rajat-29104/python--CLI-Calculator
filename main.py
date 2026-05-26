# Importing from each file 

from add import add
from subtract import subtract
from multiply import multiply
from divide import divide
from power import power

from square_root import square_root
from sin import sine
from cos import cosine
from tan import tangent
from logarithm import logarithm, natural_log
from factorial import factorial
from pi_value import show_pi

from deg_to_rad import degrees_to_radians
from rad_to_deg import radians_to_degrees


# This function gets a right value from user 
def get_number(message):
    while True:
        try:
            num = float(input(message))
            return num
        except ValueError:
            print("  Please enter a valid number!")

def main():

    print("\n========== SCIENTIFIC CALCULATOR ==========")
    print("        Built Using Python")
    print("==========================================")

    while True:

        print("\n1. Basic Arithmetic")
        print("2. Scientific Functions")
        print("3. Conversions")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        # BASIC OPERATIONS

        if choice == "1":

            a = get_number("  Enter first number:  ")
            b = get_number("  Enter second number: ")

            operation = input(
                "  Enter operation (+, -, *, /, ^): "
            )

            if operation == "+":
                add(a, b)

            elif operation == "-":
                subtract(a, b)

            elif operation == "*":
                multiply(a, b)

            elif operation == "/":
                divide(a, b)

            elif operation == "^":
                power(a, b)

            else:
                print("  Invalid operation!")

        # SCIENTIFIC 

        elif choice == "2":

            operation = input(
                "\nEnter operation "
                "(sin/cos/tan/log/ln/sqrt/fact/pi): "
            ).lower()

            if operation == "sin":
                a = get_number("  Enter angle: ")
                sine(a)

            elif operation == "cos":
                a = get_number("  Enter angle: ")
                cosine(a)

            elif operation == "tan":
                a = get_number("  Enter angle: ")
                tangent(a)

            elif operation == "log":
                a = get_number("  Enter number: ")
                logarithm(a)

            elif operation == "ln":
                a = get_number("  Enter number: ")
                natural_log(a)

            elif operation == "sqrt":
                a = get_number("  Enter number: ")
                square_root(a)

            elif operation == "fact":
                a = get_number("  Enter whole number: ")
                factorial(a)

            elif operation == "pi":
                show_pi()

            else:
                print("  Invalid operation!")

        # CONVERSIONS 

        elif choice == "3":

            operation = input(
                "\nEnter conversion "
                "(deg-rad / rad-deg): "
            ).lower()

            if operation == "deg-rad":
                a = get_number("  Enter degrees: ")
                degrees_to_radians(a)

            elif operation == "rad-deg":
                a = get_number("  Enter radians: ")
                radians_to_degrees(a)

            else:
                print("  Invalid conversion!")

        # EXIT 

        elif choice == "4":
            print("\nThank you for using calculator!")
            break

        else:
            print("\nInvalid choice!")

        input("\nPress Enter to continue...")


# ── Start the program ─────────────────────────────────────────────────────────
# This line means: only run main() if we run THIS file directly.
# Not when some other file imports from it.

if __name__ == "__main__":
    main()
