def readImage(filepath):
    with open(filepath, "r") as image:
        imageType = image.readline().strip()
        assert imageType == "P2", "Não é P2"
        
        line = image.readline().strip()
        
        width, height = map(int, line.split())
        grayscaleBits = int(image.readline().strip())
        
        pixels = []
        for _ in range(height):
            row = []
            for _ in range(width):
                for value in image.readline().split():
                    row.append(int(value))
            pixels.append(row)
        
    return pixels, width, height

def resize(pixels, width, height, multy, multx):
    newHeight = int(height * multy)
    newWidth = int(width * multx)
        
    resizedPixels = []
    for y in range(newHeight):
        newRow = []
        for x in range(newWidth):
            pixelX = int(x // multx)
            pixelY = int(y // multy)
                
            chosenPixel = pixels[pixelY][pixelX]
            newRow.append(chosenPixel)
        
        resizedPixels.append(newRow)
    
    return resizedPixels, newWidth, newHeight

def saveIMG(filename, pixels, width, height):
    with open(filename, "w") as newImage:
        newImage.write("P2\n")
        newImage.write(str(width) + " " + str(height) + "\n")
        newImage.write("255\n")
        
        for row in pixels:
            newImage.write(" ".join(map(str, row)) + "\n")
            
originalIMG = "Entrada_EscalaCinza.pgm"

pixels, width, height = readImage(originalIMG)

resizedPixels, newWidth, newHeight = resize(pixels, width, height, 0.9, 1.6)

output = "newIMG720p.pgm"
saveIMG(output, resizedPixels, newWidth, newHeight)