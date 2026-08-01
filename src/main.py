from datetime import date
from utils import add, subtract, multiply, divide, modulus, power


OPERATIONS = {
	"add": add,
	"subtract": subtract,
	"multiply": multiply,
	"divide": divide,
	"modulus": modulus,
	"power": power,
}


def get_number(prompt: str) -> float:
	return float(input(prompt))


def main() -> None:
	print("Efat Khan")
	print(date.today().isoformat())

	operation_name = input("Choose an operation (add, subtract, multiply, divide, modulus, power): ").strip().lower()
	operation = OPERATIONS.get(operation_name)

	if operation is None:
		print("Invalid operation")
		return

	first_number = get_number("Enter the first number: ")
	second_number = get_number("Enter the second number: ")

	try:
		print(operation(first_number, second_number))
	except ZeroDivisionError:
		print("Cannot divide by zero")

if __name__ == "__main__":
	main()
