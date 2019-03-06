# Part = {"type": [price, stock]}

Processor = {"p3": [100, 10], "p5": [120,10], "p7": [200, 10]}
RAM = {"16GB": [75, 10], "32GB": [150, 10]}
Storage = {"1TB": [50, 10], "2TB": [100, 10]}
Screen = {"19'": [65, 10], "23'": [120, 10]}
Case = {"Mini Tower": [40, 10], "Midi Tower": [70, 10]}
USB_Port = {"2": [10, 10], "4": [20, 10]}

def clientChoice():
    print("Choose A Processor")
    for each in Processor:
        print(each, end=', ')
    print()

    uProc = input("Chose Processor [Case Sensitive]: ")

    print("Choose RAM")
    for each in RAM:
        print(each, end=', ')
    print()

    uRAM = input("Chose RAM [Case Sensitive]: ")

    print("Choose A Storage")
    for each in Storage:
        print(each, end=', ')
    print()

    uStor = input("Chose Storage [Case Sensitive]: ")

    print("Choose A Screen")
    for each in Screen:
        print(each, end=',')
    print()

    uScreen= input("Chose Screen [Case Sensitive]: ")

    print("Choose A Processor")
    for each in Processor:
        print(each, end=', ')
    print()

    uProc = input("Chose Processor [Case Sensitive]: ")

