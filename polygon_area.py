def get_intials(name):
    name_splitter = name.split()
    intial = f"{name_splitter[0][0]}.{name_splitter[1][0]}."
    return intial

def main():
    print(get_intials("Aziz Kane"))
    
if __name__ == "__main__":
    main()
