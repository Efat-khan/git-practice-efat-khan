from datetime import date
from utils import add, subtract

def main() -> None:
	print("Efat Khan")
	print(date.today().isoformat())
	print(add(100, 3))
	print(subtract(10, 40))

if __name__ == "__main__":
	main()
