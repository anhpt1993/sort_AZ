# sort in ascending order

def input_data():
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
            break
        except ValueError:
            print("Invalid input. Try again! \n")

def sorted_list(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
    

if __name__ == '__main__':
    number = []
    for i in range(9):
        number.append(input_data())
    print(sorted_list(number))