def gridSize_def():
    global gridSize
    global grids
    while True:
        try:
            gridSize = int(input("Skriv in bredd och höjd på bädet\n"))
            if gridSize<4:
                print ("Det måste vara större än 3")
            else:
                break
        except ValueError:
            print ("Det måste vara en siffra")
    grids = [[] for _ in range (gridSize)]

    for i in range(0,gridSize):
        grids[i-1]=[0 for _ in range(gridSize)]

    return grids

def placering():
    def utritning():
        print (*list(range(0, gridSize+1)))
        for j in range (0,gridSize):
            print (*[j+1]+grids[j])
    for i in range(0,gridSize):
        utritning()
        placering = int(input("Vart vill du plasera ditt troll på rad" + " " + str(i+1) + ":"))
        grids[i][placering-1] = 1 
    utritning()

def radKoll():
    klarat = True
    for rows in range(0,gridSize):
        if [rows+1]+grids[rows] == [rows+1]+grids[rows-1]:
            klarat = False
        else:
            klarat = True
    if klarat == True:
        print("Du har klarat det :)")
    else:
        print("Du klarade det inte")


grids = gridSize_def()
placering()
radKoll()