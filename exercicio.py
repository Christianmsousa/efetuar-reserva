
# =========================================
# Janela Esquerda
janela01 = ["Janela 1","Esquerda",1] 
janela02 = ["Janela 2","Esquerda",1] 
janela03 = ["Janela 3","Esquerda",1] 
janela04 = ["Janela 4","Esquerda",1] 
janela05 = ["Janela 5","Esquerda",1] 
janela06 = ["Janela 6","Esquerda",1] 
janela07 = ["Janela 7","Esquerda",1] 
janela08 = ["Janela 8","Esquerda",1] 
janela09 = ["Janela 9","Esquerda",1] 
janela10 = ["Janela 10","Esquerda",1] 
janela11 = ["Janela 11","Esquerda",1] 
janela12 = ["Janela 12","Esquerda",1] 

# =========================================
# Janela Direita

janelaD01 = ["Janela 1","Direita",1] 
janelaD02 = ["Janela 2","Direita",1] 
janelaD03 = ["Janela 3","Direita",1] 
janelaD04 = ["Janela 4","Direita",1] 
janelaD05 = ["Janela 5","Direita",1] 
janelaD06 = ["Janela 6","Direita",1] 
janelaD07 = ["Janela 7","Direita",1] 
janelaD08 = ["Janela 8","Direita",1] 
janelaD09 = ["Janela 9","Direita",1] 
janelaD10 = ["Janela 10","Direita",1] 
janelaD11 = ["Janela 11","Direita",1] 
janelaD12 = ["Janela 12","Direita",1] 


# =========================================
# Corredor Esquerdo

Corredor01 = ["Corredor 1","Esquerdo",1] 
Corredor02 = ["Corredor 2","Esquerdo",1] 
Corredor03 = ["Corredor 3","Esquerdo",1] 
Corredor04 = ["Corredor 4","Esquerdo",1] 
Corredor05 = ["Corredor 5","Esquerdo",1] 
Corredor06 = ["Corredor 6","Esquerdo",1] 
Corredor07 = ["Corredor 7","Esquerdo",1] 
Corredor08 = ["Corredor 8","Esquerdo",1] 
Corredor09 = ["Corredor 9","Esquerdo",1] 
Corredor10 = ["Corredor 10","Esquerdo",1] 
Corredor11 = ["Corredor 11","Esquerdo",1] 
Corredor12 = ["Corredor 12","Esquerdo",1] 

# =========================================
# Corredor Direito

CorredorD01 = ["Corredor 1","Direito",1] 
CorredorD02 = ["Corredor 2","Direito",1] 
CorredorD03 = ["Corredor 3","Direito",1] 
CorredorD04 = ["Corredor 4","Direito",1] 
CorredorD05 = ["Corredor 5","Direito",1] 
CorredorD06 = ["Corredor 6","Direito",1] 
CorredorD07 = ["Corredor 7","Direito",1] 
CorredorD08 = ["Corredor 8","Direito",1] 
CorredorD09 = ["Corredor 9","Direito",1] 
CorredorD10 = ["Corredor 10","Direito",1] 
CorredorD11 = ["Corredor 11","Direito",1] 
CorredorD12 = ["Corredor 12","Direito",1] 

# =========================================
# Mensagem

linha = ("'="*30)
msgC = "(1) Consultar;"
msgE = "(2) Efetuar reservas;"
msgS = "(3) Sair;"

# =========================================
while (True):
    print("Escolha uma opção abaixo: ")
    print(linha)
    print(msgC)
    print(msgE)
    print(msgS)
    opcao = int(input())

    if opcao == 1:
        print("Consulta")
        print("(1) Janela Esquerda: ")
        print("(2) Janela Direita;")
        print("(3) Corredor Esquerdo;")
        print("(4) Corredor Direito;") 
        op1 = int(input())  
        if op1 < 1 or op1 > 4:
            print("Esta opção nao existe")
        if op1 == 1:
            print(janela01[op1-1],janela01[1],"vagas :",janela01[2])
            print(janela02[op1-1],janela02[1],"vagas :",janela02[2])
            print(janela03[op1-1],janela03[1],"vagas :",janela03[2])
            print(janela04[op1-1],janela04[1],"vagas :",janela04[2])
            print(janela05[op1-1],janela05[1],"vagas :",janela05[2])
            print(janela06[op1-1],janela06[1],"vagas :",janela06[2])
            print(janela07[op1-1],janela07[1],"vagas :",janela07[2])
            print(janela08[op1-1],janela08[1],"vagas :",janela08[2])
            print(janela09[op1-1],janela09[1],"vagas :",janela09[2])
            print(janela10[op1-1],janela10[1],"vagas :",janela10[2])
            print(janela11[op1-1],janela11[1],"vagas :",janela11[2])
            print(janela12[op1-1],janela12[1],"vagas :",janela12[2])    

        if op1 == 2:
            print(janelaD01[op1-2],janelaD01[1],"vagas :",janelaD01[2])
            print(janelaD02[op1-2],janelaD02[1],"vagas :",janelaD02[2])
            print(janelaD03[op1-2],janelaD03[1],"vagas :",janelaD03[2])
            print(janelaD04[op1-2],janelaD04[1],"vagas :",janelaD04[2])
            print(janelaD05[op1-2],janelaD05[1],"vagas :",janelaD05[2])
            print(janelaD06[op1-2],janelaD06[1],"vagas :",janelaD06[2])
            print(janelaD07[op1-2],janelaD07[1],"vagas :",janelaD07[2])
            print(janelaD08[op1-2],janelaD08[1],"vagas :",janelaD08[2])
            print(janelaD09[op1-2],janelaD09[1],"vagas :",janelaD09[2])
            print(janelaD10[op1-2],janelaD10[1],"vagas :",janelaD10[2])
            print(janelaD11[op1-2],janelaD11[1],"vagas :",janelaD11[2])
            print(janelaD12[op1-2],janelaD12[1],"vagas :",janelaD12[2])    

        if op1 == 3:
            print(Corredor01[op1-3],Corredor01[1],"vagas :",Corredor01[2])
            print(Corredor02[op1-3],Corredor02[1],"vagas :",Corredor02[2])
            print(Corredor03[op1-3],Corredor03[1],"vagas :",Corredor03[2])
            print(Corredor04[op1-3],Corredor04[1],"vagas :",Corredor04[2])
            print(Corredor05[op1-3],Corredor05[1],"vagas :",Corredor05[2])
            print(Corredor06[op1-3],Corredor06[1],"vagas :",Corredor06[2])
            print(Corredor07[op1-3],Corredor07[1],"vagas :",Corredor07[2])
            print(Corredor08[op1-3],Corredor08[1],"vagas :",Corredor08[2])
            print(Corredor09[op1-3],Corredor09[1],"vagas :",Corredor09[2])
            print(Corredor10[op1-3],Corredor10[1],"vagas :",Corredor10[2])
            print(Corredor11[op1-3],Corredor11[1],"vagas :",Corredor11[2])
            print(Corredor12[op1-3],Corredor12[1],"vagas :",Corredor12[2])

        if op1 == 4:
            print(CorredorD01[op1-4],CorredorD01[1],"vagas :",CorredorD01[2])
            print(CorredorD02[op1-4],CorredorD02[1],"vagas :",CorredorD02[2])
            print(CorredorD03[op1-4],CorredorD03[1],"vagas :",CorredorD03[2])
            print(CorredorD04[op1-4],CorredorD04[1],"vagas :",CorredorD04[2])
            print(CorredorD05[op1-4],CorredorD05[1],"vagas :",CorredorD05[2])
            print(CorredorD06[op1-4],CorredorD06[1],"vagas :",CorredorD06[2])
            print(CorredorD07[op1-4],CorredorD07[1],"vagas :",CorredorD07[2])
            print(CorredorD08[op1-4],CorredorD08[1],"vagas :",CorredorD08[2])
            print(CorredorD09[op1-4],CorredorD09[1],"vagas :",CorredorD09[2])
            print(CorredorD10[op1-4],CorredorD10[1],"vagas :",CorredorD10[2])
            print(CorredorD11[op1-4],CorredorD11[1],"vagas :",CorredorD11[2])
            print(CorredorD12[op1-4],CorredorD12[1],"vagas :",CorredorD12[2])

    elif opcao == 2:
        print("Reservar")
        print("(1) Janela Esquerda: ")
        print("(2) Janela Direita;")
        print("(3) Corredor Esquerdo;")
        print("(4) Corredor Direito;") 
        op2 = int(input())  
        if op2 < 1 or op2 > 4:
            print("Esta opção nao existe")

# =============================================================
# Janela Esqueda

        if op2 == 1:
            janelaE = input("Digite qual poltrona: ")
            if janelaE == janela01[0]:
                if janela01[2] > 0:
                    janela01[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")

            if janelaE == janela02[0]:
                if janela02[2] > 0:
                    janela02[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")

            if janelaE == janela03[0]:
                if janela03[2] > 0:
                    janela03[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")


            if janelaE == janela04[0]:
                if janela04[2] > 0:
                    janela04[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")

            if janelaE == janela05[0]:
                if janela05[2] > 0:
                    janela05[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")


            if janelaE == janela06[0]:
                if janela06[2] > 0:
                    janela06[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")


            if janelaE == janela07[0]:
                if janela07[2] > 0:
                    janela07[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")


            if janelaE == janela08[0]:
                if janela08[2] > 0:
                    janela08[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")


            if janelaE == janela09[0]:
                if janela09[2] > 0:
                    janela09[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")


            if janelaE == janela10[0]:
                if janela10[2] > 0:
                    janela10[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")


            if janelaE == janela11[0]:
                if janela11[2] > 0:
                    janela11[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")

            if janelaE == janela12[0]:
                if janela12[2] > 0:
                    janela12[2] -= 1
                    print("(1) Reserva confirmada na janela Esquerda")
                else:
                    print("(2) Vaga esgotada ")

# =================================================================================================
# Janela Direita

        if op2 == 2:
            janelaD = input("Digite qual poltrona: ")


            if janelaD == janelaD01[0]:
                if janelaD01[2] > 0:
                    janelaD01[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD02[0]:
                if janelaD02[2] > 0:
                    janelaD02[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD03[0]:
                if janelaD03[2] > 0:
                    janelaD03[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD04[0]:
                if janelaD04[2] > 0:
                    janelaD04[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD05[0]:
                if janelaD05[2] > 0:
                    janelaD05[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD06[0]:
                if janelaD06[2] > 0:
                    janelaD06[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD07[0]:
                if janelaD07[2] > 0:
                    janelaD07[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD08[0]:
                if janelaD08[2] > 0:
                    janelaD08[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD09[0]:
                if janelaD09[2] > 0:
                    janelaD09[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD10[0]:
                if janelaD10[2] > 0:
                    janelaD10[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD11[0]:
                if janelaD11[2] > 0:
                    janelaD11[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

            if janelaD == janelaD12[0]:
                if janelaD12[2] > 0:
                    janelaD12[2] -= 1
                    print("(1) Reserva confirmada na janela Direita")
                else:
                    print("(2) Vaga esgotada ")

# =================================================================================================
# Corredor Esquerdo

        if op2 == 3:
            corredor = input("Digite qual poltrona: ")


            if corredor == Corredor01[0]:
                if Corredor01[2] > 0:
                    Corredor01[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor02[0]:
                if Corredor02[2] > 0:
                    Corredor02[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor03[0]:
                if Corredor03[2] > 0:
                    Corredor03[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor04[0]:
                if Corredor04[2] > 0:
                    Corredor04[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor05[0]:
                if Corredor05[2] > 0:
                    Corredor05[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor06[0]:
                if Corredor06[2] > 0:
                    Corredor06[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor07[0]:
                if Corredor07[2] > 0:
                    Corredor07[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor08[0]:
                if Corredor08[2] > 0:
                    Corredor08[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor09[0]:
                if Corredor09[2] > 0:
                    Corredor09[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor10[0]:
                if Corredor10[2] > 0:
                    Corredor10[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor11[0]:
                if Corredor11[2] > 0:
                    Corredor11[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

            if corredor == Corredor12[0]:
                if Corredor12[2] > 0:
                    Corredor12[2] -= 1
                    print("(1) Reserva confirmada no corredor Esquerdo")
                else:
                    print("(2) Vaga esgotada ")

# =================================================================================================
# Corredor Direito

        if op2 == 4:
            corredorD = input("Digite qual poltrona: ")

            if corredorD == CorredorD01[0]:
                if CorredorD01[2] > 0:
                    CorredorD01[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
                
            if corredorD == CorredorD02[0]:
                if CorredorD02[2] > 0:
                    CorredorD02[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
                
            if corredorD == CorredorD03[0]:
                if CorredorD03[2] > 0:
                    CorredorD03[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
               
            if corredorD == CorredorD04[0]:
                if CorredorD04[2] > 0:
                    CorredorD04[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    

            if corredorD == CorredorD05[0]:
                if CorredorD05[2] > 0:
                    CorredorD05[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
 
            if corredorD == CorredorD06[0]:
                if CorredorD06[2] > 0:
                    CorredorD06[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
 
            if corredorD == CorredorD07[0]:
                if CorredorD07[2] > 0:
                    CorredorD07[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
 
            if corredorD == CorredorD08[0]:
                if CorredorD08[2] > 0:
                    CorredorD08[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
 
            if corredorD == CorredorD09[0]:
                if CorredorD09[2] > 0:
                    CorredorD09[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
 
            if corredorD == CorredorD10[0]:
                if CorredorD10[2] > 0:
                    CorredorD10[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
 
            if corredorD == CorredorD11[0]:
                if CorredorD11[2] > 0:
                    CorredorD11[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
 
            if corredorD == CorredorD12[0]:
                if CorredorD12[2] > 0:
                    CorredorD12[2] -= 1
                    print("(1) Reserva confirmada no corredor Direito")
                else:
                    print("(2) Vaga esgotada ")                    
 
    else:
        break