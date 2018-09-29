def choose(n, k):
    combinations = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    return combinations

if __name__ == "__main__":
    import sys
    import math
    deckSize = int(input("Deck size: "))
    numLands = int(input("Number of lands: "))
    numOneDrops = int(input("Number of 1 mana cards: "))
    
    oddsOfNotDrawingLand = choose(deckSize - numLands, 7) / choose(deckSize, 7)
    oddsOfDrawingLand = 1 - oddsOfNotDrawingLand
    
    oddsOfNotDrawingOneDrop = choose(deckSize - numOneDrops, 7) / choose(deckSize, 7)
    oddsOfDrawingOneDrop = 1 - oddsOfNotDrawingOneDrop
    
    print("Odds of drawing atleast one land: %.2f" % (oddsOfDrawingLand*100))
    print("Odds of drawing atleast one 1 mana card: %.2f" % (oddsOfDrawingOneDrop*100))
    
    notDrawingOneDropAndLand = oddsOfNotDrawingLand + oddsOfNotDrawingOneDrop
    drawingOneDropAndLand = 1 - notDrawingOneDropAndLand
    
    print("Odds of drawing atleast one 1 mana card AND atleast one land: %.2f" % (drawingOneDropAndLand*100))