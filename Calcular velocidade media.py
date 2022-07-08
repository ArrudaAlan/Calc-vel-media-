while True:
    print('''    [ 1 ] Velocidade média
    [ 2 ] Deslocamento
    [ 3 ] Intervalo de Tempo
    [ 4 ] sair do programa''')
    opc = int(input('Qual a sua opção? '))
    if opc == 1: #velocidae media
       print(''' selecione a unidade de medida da resposta que deseja:
        [ 1 ] m/s
        [ 2 ] km/h''')
       opcuni = int(input('Qual a sua opção? '))
       if opcuni == 1: #resposta em m/s
           print('''Deseja transformar alguma unidade?
           [ 1 ] km para m
           [ 2 ] h para s
           [ 3 ] km e h para m e s
           [ 4 ] não desejo''')
           opctrans = int(input('qual a sua opção? '))
           if opctrans == 1:
               d = float(input('Digite o deslocamento em km: '))
               t = float(input('Digite o tempo em s: '))
               vm = ( d * 1000 ) / t
               print(f'Sua velocidade média é de {vm:.2f} m/s')
           elif opctrans == 2:
               d = float(input('Digite o deslocamento em m: '))
               t = float(input('Digite o tempo em h: '))
               vm = d / ( t * 3600)
               print(f'Sua velocidade média é de {vm:.2f} m/s')
           elif opctrans == 3:
               d = float(input('Digite o descolamento em km: '))
               t = float(input('Digite o tempo em h: '))
               vm = ( d / t ) / 3.6
               print(f'Sua velocidade média é de {vm:.2f} m/s')
           elif opctrans == 4:
               d = float(input('Digite o descolamento em m: '))
               t = float(input('Digite o tempo em s: '))
               vm = d / t
               print(f'Sua velocidade média é de {vm:.2f} m/s')
           else:
               while True:
                   print('Desculpe não entendi, pode repetir?')
                   print('''Deseja transformar alguma unidade?
                              [ 1 ] km para m
                              [ 2 ] h para s
                              [ 3 ] km e h para m e s
                              [ 4 ] não desejo''')
                   opctrans = int(input('qual a sua opção? '))
                   if opctrans == 1:
                       d = float(input('Digite o deslocamento em km: '))
                       t = float(input('Digite o tempo em s: '))
                       vm = (d * 1000) / t
                       print(f'Sua velocidade média é de {vm:.2f} m/s')
                       break
                   elif opctrans == 2:
                       d = float(input('Digite o deslocamento em m: '))
                       t = float(input('Digite o tempo em h: '))
                       vm = d / (t * 3600)
                       print(f'Sua velocidade média é de {vm:.2f} m/s')
                       break
                   elif opctrans == 3:
                       d = float(input('Digite o descolamento em km: '))
                       t = float(input('Digite o tempo em h: '))
                       vm = (d / t) / 3.6
                       print(f'Sua velocidade média é de {vm:.2f} m/s')
                       break
                   elif opctrans == 4:
                       d = float(input('Digite o descolamento em m: '))
                       t = float(input('Digite o tempo em s: '))
                       vm = d / t
                       print(f'Sua velocidade média é de {vm:.2f} m/s')
                       break
       elif opcuni == 2: #resposta em km/h
           print('''Deseja transformar alguma unidade?
                      [ 1 ] m para km
                      [ 2 ] s para h
                      [ 3 ] m e s para km e h
                      [ 4 ] não desejo''')
           opctrans = int(input('Qual a sua opção? '))
           if opctrans == 1:
               d = float(input('Digite o deslocamento em m: '))
               t = float(input('Digite o tempo em h: '))
               vm = (d / 1000) / t
               print(f'Sua velocidade média é de {vm:.2f} km/h')
           elif opctrans == 2:
               d = float(input('Digite o deslocamento em km: '))
               t = float(input('Digite o tempo em s: '))
               vm = d / (t / 3600)
               print(f'Sua velocidade média é de {vm:.2f} km/h')
           elif opctrans == 3:
               d = float(input('Digite o descolamento em m: '))
               t = float(input('Digite o tempo em s: '))
               vm = (d / t) * 3.6
               print(f'Sua velocidade média é de {vm:.2f} km/h')
           elif opctrans == 4:
               d = float(input('Digite o descolamento em km: '))
               t = float(input('Digite o tempo em h: '))
               vm = d / t
               print(f'Sua velocidade média é de {vm:.2f} km/h')
           else:
               while True:
                   print('Desculpe não entendi, pode repetir?')
                   print('''Deseja transformar alguma unidade?
                              [ 1 ] m para km
                              [ 2 ] s para h
                              [ 3 ] m e s para km e h
                              [ 4 ] não desejo''')
                   opctrans = int(input('Qual a sua opção? '))
                   if opctrans == 1:
                       d = float(input('Digite o deslocamento em m: '))
                       t = float(input('Digite o tempo em h: '))
                       vm = (d / 1000) / t
                       print(f'Sua velocidade média é de {vm:.2f} km/h')
                       break
                   elif opctrans == 2:
                       d = float(input('Digite o deslocamento em km: '))
                       t = float(input('Digite o tempo em s: '))
                       vm = d / (t / 3600)
                       print(f'Sua velocidade média é de {vm:.2f} km/h')
                       break
                   elif opctrans == 3:
                       d = float(input('Digite o descolamento em m: '))
                       t = float(input('Digite o tempo em s: '))
                       vm = (d / t) * 3.6
                       print(f'Sua velocidade média é de {vm:.2f} km/h')
                       break
                   elif opctrans == 4:
                       d = float(input('Digite o descolamento em km: '))
                       t = float(input('Digite o tempo em h: '))
                       vm = d / t
                       print(f'Sua velocidade média é de {vm:.2f} km/h')
                       break
    elif opc == 2: #deslocamento
        print('''Selecione a unidade de medidade que deseja da resposta: 
        [ 1 ] m
        [ 2 ] km''')
        opcuni = int(input('Qual a sua opção? '))
        if opcuni == 1: #deslocamento em m
            print(''' Deseja transformar alguma unidade? 
            [ 1 ] km/h para m/s
            [ 2 ] h para s
            [ 3 ] km/h e h para m/s e s
            [ 4 ] não desejo''')
            opctrans = int(input("Qual sua opção? "))
            if opctrans == 1:
                vm = float(input('Digite sua velocidade média em km/h: '))
                t = float(input('Digite o tempo em s: '))
                d = (vm / 3.6) * t
                print(f'O deslocamento foi de {d:.2f}m')
            elif opctrans == 2:
                vm = float(input('Digite sua velocidade média em m/s: '))
                t = float(input('Digite seu tempo em h: '))
                d = vm * (t * 3600)
                print(f'O deslocamento foi de {d:.2f}m')
            elif opctrans == 3:
                vm = float(input('Digite sua velocidade média em km/h: '))
                t = float(input('Digite seu tempo em h: '))
                d = (vm*t)*1000
                print(f'O deslocamento foi de {d:.2f}m')
            elif opctrans == 4:
                vm = float(input('Digite sua velocidade média em m/s: '))
                t = float(input('Digite seu tempo em s: '))
                d = vm*t
                print(f'Seu deslocamento foi de {d:.2f}m')
            else:
                while True:
                    print('Desculpe não entendi, pode repetir?')
                    print(''' Deseja transformar alguma unidade? 
                                [ 1 ] km/h para m/s
                                [ 2 ] h para s
                                [ 3 ] km/h e h para m/s e s
                                [ 4 ] não desejo''')
                    opctrans = int(input("Qual sua opção? "))
                    if opctrans == 1:
                        vm = float(input('Digite sua velocidade média em km/h: '))
                        t = float(input('Digite o tempo em s: '))
                        d = (vm / 3.6) * t
                        print(f'O deslocamento foi de {d:.2f}m')
                        break
                    elif opctrans == 2:
                        vm = float(input('Digite sua velocidade media em m/s: '))
                        t = float(input('Digite seu tempo em h: '))
                        d = vm * (t * 3600)
                        print(f'O deslocamento foi de {d:.2f}m')
                        break
                    elif opctrans == 3:
                        vm = float(input('Digite sua velocidade média em km/h: '))
                        t = float(input('Digite seu tempo em h: '))
                        d = (vm * t) * 1000
                        print(f'O deslocamento foi de {d:.2f}m')
                        break
                    elif opctrans == 4:
                        vm = float(input('Digite sua velocidade media em m/s: '))
                        t = float(input('Digite seu tempo em s: '))
                        d = vm * t
                        print(f'Seu deslocamento foi de {d:.2f}m')
                        break
        elif opcuni == 2: #deslocamento em km
            print(''' Deseja transformar alguma unidade? 
                        [ 1 ] m/s para km/h
                        [ 2 ] s para h
                        [ 3 ] m/s e s para km/h e h
                        [ 4 ] não desejo''')
            opctrans = int(input("Qual sua opção? "))
            if opctrans == 1:
                vm = float(input('Digite sua velocidade média em m/s: '))
                t = float(input('Digite o tempo em h: '))
                d = (vm * 3.6) * t
                print(f'O deslocamento foi de {d:.2f}km')
            elif opctrans == 2:
                vm = float(input('Digite sua velocidade média em km/h: '))
                t = float(input('Digite seu tempo em s: '))
                d = vm * (t / 3600)
                print(f'O deslocamento foi de {d:.2f}km')
            elif opctrans == 3:
                vm = float(input('Digite sua velocidade média em m/s: '))
                t = float(input('Digite seu tempo em s: '))
                d = (vm * t) / 1000
                print(f'O deslocamento foi de {d:.2f}km')
            elif opctrans == 4:
                vm = float(input('Digite sua velocidade média em km/h: '))
                t = float(input('Digite seu tempo em h: '))
                d = vm * t
                print(f'Seu deslocamento foi de {d:.2f}km')
            else:
                while True:
                    print('Desculpe não entendi, pode repetir?')
                    print(''' Deseja transformar alguma unidade? 
                                [ 1 ] m/s para km/h
                                [ 2 ] s para h
                                [ 3 ] m/s e s para km/h e h
                                [ 4 ] não desejo''')
                    opctrans = int(input("Qual sua opção? "))
                    if opctrans == 1:
                        vm = float(input('Digite sua velocidade média em m/s: '))
                        t = float(input('Digite o tempo em h: '))
                        d = (vm * 3.6) * t
                        print(f'O deslocamento foi de {d:.2f}km')
                        break
                    elif opctrans == 2:
                        vm = float(input('Digite sua velocidade média em km/h: '))
                        t = float(input('Digite seu tempo em s: '))
                        d = vm * (t / 3600)
                        print(f'O deslocamento foi de {d:.2f}km')
                        break
                    elif opctrans == 3:
                        vm = float(input('Digite sua velocidade média em m/s: '))
                        t = float(input('Digite seu tempo em s: '))
                        d = (vm * t) / 1000
                        print(f'O deslocamento foi de {d:.2f}km')
                    elif opctrans == 4:
                        vm = float(input('Digite sua velocidade media em km/h: '))
                        t = float(input('Digite seu tempo em h: '))
                        d = vm * t
                    print(f'Seu deslocamento foi de {d:.2f}km')
                    break
    elif opc == 3: #tempo
        print('''Selecione a unidade de medidade que deseja da resposta: 
                [ 1 ] s
                [ 2 ] h''')
        opcuni = int(input('Qual a sua opção? '))
        if opcuni == 1:  # tempo em s
            print(''' Deseja transformar alguma unidade? 
                        [ 1 ] km/h para m/s
                        [ 2 ] km para m
                        [ 3 ] km/h e h para m/s e s
                        [ 4 ] não desejo''')
            opctrans = int(input("Qual sua opção? "))
            if opctrans == 1:
                vm = float(input('Digite sua velocidade média em km/h: '))
                d = float(input('Digite seu deslocamento em m: '))
                t = d / (vm / 3.6)
                print(f'Seu tempo é de {t:.2f}s')
            elif opctrans == 2:
                vm = float(input('Digite sua velocidade média em m/s: '))
                d = float(input('Digite seu deslocamento em km: '))
                t = (d * 1000) / vm
                print(f'Seu tempo é de {t:.2f}s')
            elif opctrans == 3:
                vm = float(input('Digite sua velocidade média em km/h: '))
                d = float(input('Digite seu deslocamento em km: '))
                t = (d / vm) * 3600
                print(f'Seu tempo é de {t:.2f}s')
            elif opctrans == 4:
                vm = float(input('Digite sua velocidade média em m/s: '))
                d = float(input('Digite seu deslocamento em m: '))
                t = d / vm
                print(f'Seu tempo é de {t:.2f}s')
            else:
                while True:
                    print('Desculpe não entendi, pode repetir?')
                    print(''' Deseja transformar alguma unidade? 
                                [ 1 ] km/h para m/s
                                [ 2 ] km para m
                                [ 3 ] km/h e h para m/s e s
                                [ 4 ] não desejo''')
                    opctrans = int(input("Qual sua opção? "))
                    if opctrans == 1:
                        vm = float(input('Digite sua velocidade média em km/h: '))
                        d = float(input('Digite seu deslocamento em m: '))
                        t = d / (vm / 3.6)
                        print(f'Seu tempo é de {t:.2f}s')
                        break
                    elif opctrans == 2:
                        vm = float(input('Digite sua velocidade média em m/s: '))
                        d = float(input('Digite seu deslocamento em km: '))
                        t = (d * 1000) / vm
                        print(f'Seu tempo é de {t:.2f}s')
                        break
                    elif opctrans == 3:
                        vm = float(input('Digite sua velocidade média em km/h: '))
                        d = float(input('Digite seu deslocamento em km: '))
                        t = (d / vm) * 3600
                        print(f'Seu tempo é de {t:.2f}s')
                        break
                    elif opctrans == 4:
                        vm = float(input('Digite sua velocidade média em m/s: '))
                        d = float(input('Digite seu deslocamento em m: '))
                        t = d / vm
                        print(f'Seu tempo é de {t:.2f}s')
                        break
        elif opcuni == 2: #tempo em h
            print(''' Deseja transformar alguma unidade? 
                                    [ 1 ] m/s para km/h
                                    [ 2 ] m para km
                                    [ 3 ] m/s e s para km/h e h
                                    [ 4 ] não desejo''')
            opctrans = int(input("Qual sua opção? "))
            if opctrans == 1:
                vm = float(input('Digite sua velocidade média em m/s: '))
                d = float(input('Digite seu deslocamento em km: '))
                t = d / (vm * 3.6)
                print(f'Seu tempo é de {t:.2f}h')
            elif opctrans == 2:
                vm = float(input('Digite sua velocidade média em km/h: '))
                d = float(input('Digite seu deslocamento em m: '))
                t = (d / 1000) / vm
                print(f'Seu tempo é de {t:.2f}h')
            elif opctrans == 3:
                vm = float(input('Digite sua velocidade média em m/s: '))
                d = float(input('Digite seu deslocamento em m: '))
                t = (d / vm) / 3600
                print(f'Seu tempo é de {t:.2f}h')
            elif opctrans == 4:
                vm = float(input('Digite sua velocidade média em km/h: '))
                d = float(input('Digite seu deslocamento em h: '))
                t = d / vm
                print(f'Seu tempo é de {t:.2f}h')
            else:
                while True:
                    print('Desculpe não entendi, pode repetir?')
                    print(''' Deseja transformar alguma unidade? 
                                            [ 1 ] m/s para km/h
                                            [ 2 ] m para km
                                            [ 3 ] m/s e s para km/h e h
                                            [ 4 ] não desejo''')
                    opctrans = int(input("Qual sua opção? "))
                    if opctrans == 1:
                        vm = float(input('Digite sua velocidade média em m/s: '))
                        d = float(input('Digite seu deslocamento em km: '))
                        t = d / (vm * 3.6)
                        print(f'Seu tempo é de {t:.2f}h')
                        break
                    elif opctrans == 2:
                        vm = float(input('Digite sua velocidade média em km/h: '))
                        d = float(input('Digite seu deslocamento em m: '))
                        t = (d / 1000) / vm
                        print(f'Seu tempo é de {t:.2f}h')
                        break
                    elif opctrans == 3:
                        vm = float(input('Digite sua velocidade média em m/s: '))
                        d = float(input('Digite seu deslocamento em m: '))
                        t = (d / vm) / 3600
                        print(f'Seu tempo é de {t:.2f}h')
                        break
                    elif opctrans == 4:
                        vm = float(input('Digite sua velocidade média em km/h: '))
                        d = float(input('Digite seu deslocamento em h: '))
                        t = d / vm
                        print(f'Seu tempo é de {t:.2f}h')
                        break
    elif opc == 4:
        print('Muito obrigado por utilizar este programa!')
        break












