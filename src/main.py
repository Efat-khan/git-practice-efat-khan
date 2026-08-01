from datetime import date
from utils import add, subtract, multiply, divide, modulus, power

def main() -> None:
	print("Efat Khan")
	print(date.today().isoformat())
	print(add(100, 3))
	print(subtract(10, 40))
	print(multiply(5, 6))
	print(divide(20, 4))
	print(modulus(20, 3))
	print(power(2, 5))

if __name__ == "__main__":
	main()
