from datetime import date
from utils import add, subtract, multiply, divide

def main() -> None:
	print("Efat Khan")
	print(date.today().isoformat())
	print(add(100, 3))
	print(subtract(10, 40))
	print(multiply(5, 6))
	print(divide(20, 4))

if __name__ == "__main__":
	main()
