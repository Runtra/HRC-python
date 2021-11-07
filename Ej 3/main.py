def main():
    currencies = {
            "peso" : "$",
            "dolar" : "U$S",
            "yen" : "¥"
            }
    str = input("Ingrese una divisa:").lower() 
    print()

    if str in currencies:
        print(f"La divisa {str} tiene el siguiente simbolo: {currencies[str]}")
    else:
        print("La divisa ingresada no esta en nuestra base de datos")

if __name__ == "__main__":
    main()

