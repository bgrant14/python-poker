import random
faces = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["♦","♣","♠","♥"]

class card:
    def __init__(this, face, suit):
        this.face = face
        this.suit = suit

    def getCard(this):
        return this.face + this.suit

class cDeck:
    def __init__(this):
        this.deck = []
        for i in range (13):
            for j in range (4):
                this.deck.append(card(faces[i], suits[j]))

    def moveCard(this):
        randLoc = random.randrange(0,len(this.deck))
        tempCard = this.deck[randLoc]
        this.deck.pop(randLoc)
        return tempCard 

    def getDeck(this):
        return this.deck

newDeck = cDeck()

class hand:
    def __init__(this):
        this.myHand = []
        for i in range(4):
            this.myHand.append(newDeck.moveCard())

    def showHand(this):
        for i in this.myHand:
            print(i.getCard() )
    
    def getHand(this):
        return this.myHand

class game:
    def __init__(this, players):
        this.hands = []
        for i in range(players):
            this.hands.append(hand())
        this.board = [newDeck.moveCard(), newDeck.moveCard(), newDeck.moveCard()]
        chips = 100

    def p1Hand(this):
        this.hands[0].showHand()

    def showBoard(this):
        for i in this.board:
            print(i.getCard())

    def allHands(this):
        for i in this.hands:
            i.showHand()

    def run(this):
        print("Hand:")
        newGame.allHands()
        print("Board:")
        newGame.showBoard()

newGame = game(10)

newGame.run()
