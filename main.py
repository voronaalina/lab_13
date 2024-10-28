from sweet import SWEET
def main():
    candy1 = SWEET("шоколадка", 29.90, "Roshen")
    candy2 = SWEET("мармелад", 23.0, "ABK")
    candy3 = SWEET("пончик", 17.0, "КОНТІ")

    print("властивості цукерок:")
    candy1.display()
    candy2.display()
    candy3.display()

    candy1.set_name("білий шоколад")
    candy1.set_price(32.0)
    print("оновлена назва:",candy1.get_name(), " оновлена ціна:",candy1.get_price())
if __name__ == "__main__":
     main()
