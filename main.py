import random


def main():
    total = 0
    numbers = []
    while True:
        num = random.randint(1,10)
        if total + num > 100:
            break
        numbers.append(num)
        total += num

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
