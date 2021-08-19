digit_number = None
while digit_number == None:
    try:
        x = int(input("Enter digit number: "))
        if digit_number <= 0 :
            print(x)
            raise BaseException()
        digit_number = x
    except Exception as ex:
        print(ex)
        print("input number not a posetive integer")
