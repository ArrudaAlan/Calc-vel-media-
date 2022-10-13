from velmedia.lib.interface import *
from velmedia.lib.arquivo import *



#arruma o while true bug letras

while True:
    print('''    [ 1 ] Velocidade média
    [ 2 ] Deslocamento
    [ 3 ] Intervalo de Tempo
    [ 0 ] sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:  # velocidae media
        while True:
            print('''Selecione a unidade de medida que deseja na resposta:
            [ 1 ] m/s
            [ 2 ] km/h
            [ 0 ] Voltar''')
            opcao_unidade = int(input('Qual a sua opção? '))
            while True:
                if opcao_unidade == 1:  # resposta em m/s
                    print('''Deseja transformar alguma unidade?
                   [ 1 ] km para m
                   [ 2 ] h para s
                   [ 3 ] km e h para m e s
                   [ 0 ] não desejo''')
                    opcao_de_transformacao = int(input('qual a sua opção? '))
                    if opcao_de_transformacao == 1:
                        ms_VelocidadeMedia_km_por_segundo()
                        break
                    elif opcao_de_transformacao == 2:
                        ms_VelocidadeMedia_metros_por_hora()
                        break
                    elif opcao_de_transformacao == 3:
                        ms_VelocidadeMedia_km_por_hora()
                        break
                    elif opcao_de_transformacao == 0:
                        ms_VelocidadeMedia_metros_por_segundo()
                        break
                    else:
                        print('Digite um valor válido!')
            elif opcao_unidade == 2:  # resposta em km/h
                while True:
                    print('''Deseja transformar alguma unidade?
                              [ 1 ] m para km
                              [ 2 ] s para h
                              [ 3 ] m e s para km e h
                              [ 0 ] não desejo''')
                    opcao_de_transformacao = int(input('Qual a sua opção? '))
                    if opcao_de_transformacao == 1:
                        km_VelocidadeMedia_metros_por_hora()
                    elif opcao_de_transformacao == 2:
                        km_VelocidadeMedia_km_por_segundo()
                    elif opcao_de_transformacao == 3:
                        km_VelocidadeMedia_metros_por_segundo()
                    elif opcao_de_transformacao == 0:
                        km_VelocidadeMedia_km_por_hora()
                    else:
                        print('Digite um valor válido!')

    elif opcao == 2:  # deslocamento
        print('''Selecione a unidade de medida que deseja na resposta: 
        [ 1 ] m
        [ 2 ] km''')
        opcao_unidade = int(input('Qual a sua opção? '))
        if opcao_unidade == 1:  # deslocamento em m
            print('''Deseja transformar alguma unidade? 
            [ 1 ] km/h para m/s
            [ 2 ] h para s
            [ 3 ] km/h e h para m/s e s
            [ 0 ] não desejo''')
            opcao_de_transformacao = int(input("Qual sua opção? "))
            if opcao_de_transformacao == 1:
                metros_Deslocamento_km_por_hora_por_segundo()
            elif opcao_de_transformacao == 2:
                metros_Deslocamento_metros_por_segundo_por_hora()
            elif opcao_de_transformacao == 3:
                metros_Deslocamento_km_por_hora_por_hora()
            elif opcao_de_transformacao == 0:
                metros_Deslocamento_metros_por_segundo_por_segundo()
            else:
                metros_Deslocamento_Painel_Tranformacao_de_Unidade()
        elif opcao_unidade == 2:  # deslocamento em km
            print(''' Deseja transformar alguma unidade? 
                        [ 1 ] m/s para km/h
                        [ 2 ] s para h
                        [ 3 ] m/s e s para km/h e h
                        [ 0 ] não desejo''')
            opcao_de_transformacao = int(input("Qual sua opção? "))
            if opcao_de_transformacao == 1:
                km_Deslocamento_metros_por_segundos_por_hora()
            elif opcao_de_transformacao == 2:
                km_Deslocamento_km_por_hora_por_segundo()
            elif opcao_de_transformacao == 3:
                km_Deslocamento_metros_por_segundo_por_segundo()
            elif opcao_de_transformacao == 0:
                km_Deslocamento_km_por_hora_por_hora()
            else:
                km_Deslocamento_Painel_Tranformacao_de_unidade()
    elif opcao == 3:  # tempo
        print('''Selecione a unidade de medida que deseja na resposta: 
                [ 1 ] s
                [ 2 ] h''')
        opcao_unidade = int(input('Qual a sua opção? '))
        if opcao_unidade == 1:  # tempo em s
            print(''' Deseja transformar alguma unidade? 
                        [ 1 ] km/h para m/s
                        [ 2 ] km para m
                        [ 3 ] km/h e h para m/s e s
                        [ 0 ] não desejo''')
            opcao_de_transformacao = int(input("Qual sua opção? "))
            if opcao_de_transformacao == 1:
                segundos_Tempo_km_por_hora_por_metros()
            elif opcao_de_transformacao == 2:
                segundos_Tempo_metros_por_segundo_por_km()
            elif opcao_de_transformacao == 3:
                segundos_Tempo_km_por_hora_por_km()
            elif opcao_de_transformacao == 0:
                segundos_Tempo_metros_por_segundo_por_metros()
            else:
                segundos_Tempo_Painel_Transformacao_de_Unidade()
        elif opcao_unidade == 2:  # tempo em h
            print(''' Deseja transformar alguma unidade? 
                      [ 1 ] m/s para km/h
                      [ 2 ] m para km
                      [ 3 ] m/s e s para km/h e h
                      [ 0 ] não desejo''')
            opcao_de_transformacao = int(input("Qual sua opção? "))
            if opcao_de_transformacao == 1:
                horas_Tempo_metros_por_segundo_por_km()
            elif opcao_de_transformacao == 2:
                horas_Tempo_km_por_hora_por_metros()
            elif opcao_de_transformacao == 3:
                horas_Tempo_metros_por_segundo_por_metros()
            elif opcao_de_transformacao == 0:
                horas_Tempo_km_por_hora_por_km()
            else:
                hora_Tempo_Painel_Transformacao_de_Unidade()
    elif opcao == 0:
        print('Muito obrigado por utilizar este programa!')
        break

    else:
        print('Por favor digite um valor válido!')
