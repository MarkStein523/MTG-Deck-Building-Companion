def choose(n, k):
    combinations = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    return combinations

if __name__ == "__main__":
    import sys
    import math
    deckSize = int(input("Deck size: "))
    numLands = int(input("Number of lands: "))
    
    oddsOfNotDrawingLand = choose(deckSize - numLands, 7) / choose(deckSize, 7)
    oddsOfDrawingLand = 1 - oddsOfNotDrawingLand
    
    print("Odds of drawing atleast one land: %.2f" % (oddsOfDrawingLand*100))