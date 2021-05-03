def jogar (jogador1, jogador2, opcao1, opcao2):
    if opcao1 == "pedra" and opcao2 == "pedra":
        print("EMPATE, jogadores escolheram "+ opcao1)
    elif opcao1 == "pedra" and opcao2 == "papel":
        print("O player: "+jogador2+ " escolheu " +opcao2+" e venceu.")
    elif opcao1 == "pedra" and opcao2 == "tesoura":
        print("O player: "+jogador1+ " escolheu " +opcao1+" e venceu.")
    elif opcao1 == "papel" and opcao2 == "papel":
        print("EMPATE, jogadores escolheram "+ opcao1)
    elif opcao1 == "papel" and opcao2 == "pedra":
        print("O player: "+jogador1+ " escolheu " +opcao1+" e venceu.")
    elif opcao1 == "papel" and opcao2 == "tesoura":
        print("O player: "+jogador2+ " escolheu " +opcao2+" e venceu.")
    elif opcao1 == "tesoura" and opcao2 == "pedra":
        print("O player: "+jogador2+ " escolheu " +opcao2+" e venceu.")
    elif opcao1 == "tesoura" and opcao2 == "papel":
        print("O player: "+jogador1+ " escolheu " +opcao1+" e venceu.")
    elif opcao1 == "tesoura" and opcao2 == "tesoura":
        print("EMPATE, jogadores escolheram "+ opcao1)

        
jogar("Allan", "Mayara", "pedra", "papel")

