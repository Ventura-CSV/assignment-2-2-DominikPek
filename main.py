def main():
    celcius = int(input('Enter temperature in Celcius: '))

    fahrenheit = (9 / 5) * celcius + 32

    print(f'Temperature in Fahrenheit: {fahrenheit}')
    
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
