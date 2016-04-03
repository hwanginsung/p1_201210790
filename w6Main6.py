def rockPaperScissor(player1,player2):
    if player1=='rock':
        if player2=='rock':
            res="Same!"
        elif player2=='paper':
            res="player2 win!"
        elif player2=='scissor':
            res="player1 win!"
    elif player1=='paper':
        if player2=='rock':
            res="player1 win!"
        elif player2=='paper':
            res="Same!"
        elif player2=='scissor':
            res="player2 win!"
    elif player1=='scissor':
        if player2=='rock':
            res="player2 win!"
        elif player2=='paper':
            res="player1 win!"
        elif player2=='scissor':
            res="Same"
    print "player 1 {0:s} player 2 {1:s}, result is {2:s}".format(player1,player2,res)
    return res

player1=raw_input('RockPaperScissor : ')
player2=raw_input('RockPaperScissor : ')

result=rockPaperScissor(player1,player2)

