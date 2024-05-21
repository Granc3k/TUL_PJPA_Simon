def main():
    with open('result.txt', 'r') as file1, open('result_Jirka.txt', 'r') as file2:
        not_found = True
        for line1, line2 in zip(file1, file2):
            if line1 != line2:
                not_found = False
                print(f"Řádek v soubor1: {line1}")
                print(f"Řádek v soubor2: {line2}")
    
    if not_found:
        print("Výsledky jsou stejné")


if __name__ == "__main__":
    main()