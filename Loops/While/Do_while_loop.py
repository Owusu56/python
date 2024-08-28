
                      #WHILE
# initial  i= 0
list = ["Pauson", "Giscard", "Classical Jones"]

i = 0
while i < list.__len__():
    print(list[i], "is a software engineer.")

    i = i + 1




                      #DO WHILE

while True:
    name = input("Have you eaten this morning?")
    if name == "Nope":
        while True:
            name = input("Why haven't you eaten?")
            if name == "Nothing":
                print("Please go and eat.")

    if name == "Yes":
        print("Alright, have a good day")
        break
