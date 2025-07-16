
def main():



    listee = input ("Enter a list of numbers, divided by space: ")

    if not listee:
        print("THERE IS NO INPUT!! DO IT AGAIN!!")
        exit()

        
    haechae = listee.split()


    print(type(listee), listee)

    print(type(haechae), haechae)


if __name__ == "__main__":
    main()