def is_power_of_basis(value: int, basis: int) -> bool:
    if value == 0:
        return False
    elif value == 1:
        return True
    return value % basis == 0 and is_power_of_basis(value // basis, basis)


def main():
    values = [0, 1, 3, 4, 8, 9, 64, 81, 243, 256]
    bases = [2, 3]
    for basis in bases:
        print(f'{basis=}')
        for value in values:
            print(value, is_power_of_basis(value, basis=basis))
        print()


if __name__ == '__main__':
    main()
