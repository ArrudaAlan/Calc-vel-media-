# -----VELOCIDADE MEDIA EM M/S------

def ms_VelocidadeMedia_km_por_segundo():
    d = float(input('Digite o deslocamento em quilômetros (km): '))
    t = float(input('Digite o tempo em segundos (s): '))
    dm = (d * 1000)
    vm = (dm) / t
    print(f'Sua velocidade média é de {vm:.2f} m/s')
    while True:
        explicacao = str(input("Deseja a explicação? (s ou n)")).strip().lower()
        if explicacao == "s":
                print(f'''A velocidade média de um corpo é dada entre o intervalo do deslocamento (posição final - posição inicial), \u0394s, em determinado intervalo de tempo (tempo final - tempo inicial), \u0394t.''')
                print(f'''Logo \u0394s/\u0394t''')
                print(f'Primeiramente deve verificar as unidades, {d} está em quilômetros (km) então deve transformar para metros (m).')
                print(f'Então 1km é 1000m, então, {d} * 1000.')
                print(f'\u0394s é {dm}m')
                print(f'Vm = {dm}/{t}')
                print(f'Vm = {vm}m/s')
                break
        elif explicacao == "n":
            print("Ok!")
            break
        else:
            print('Digite valor valido!')




def ms_VelocidadeMedia_metros_por_hora():
    d = float(input('Digite o deslocamento em metros (m): '))
    t = float(input('Digite o tempo em horas (h): '))
    vm = d / (t * 3600)
    print(f'Sua velocidade média é de {vm:.2f} m/s')


def ms_VelocidadeMedia_km_por_hora():
    d = float(input('Digite o descolamento em quilômetros (km): '))
    t = float(input('Digite o tempo em horas (h): '))
    vm = (d / t) / 3.6
    print(f'Sua velocidade média é de {vm:.2f} m/s')


def ms_VelocidadeMedia_metros_por_segundo():
    d = float(input('Digite o descolamento em metros (m): '))
    t = float(input('Digite o tempo em segundos (s): '))
    vm = d / t
    print(f'Sua velocidade média é de {vm:.2f} m/s')


def ms_VelocidadeMedia_Transformacao_de_Unidade():
    while True:
        print('Desculpe não entendi, pode repetir?')
        print('''Deseja transformar alguma unidade?
                   [ 1 ] Quilômetros (km) para metros (m)
                   [ 2 ] Hora (h) para segundos (s)
                   [ 3 ] Quilômetros (km) e hora (h) para metros (m) e segundos (s)
                   [ 0 ] Não desejo''')
        opcao_de_transformacao = int(input('qual a sua opção? '))
        if opcao_de_transformacao == 1:
            d = float(input('Digite o deslocamento em quilômetros (km): '))
            t = float(input('Digite o tempo em segundos (s): '))
            vm = (d * 1000) / t
            print(f'Sua velocidade média é de {vm:.2f} m/s')
            break
        elif opcao_de_transformacao == 2:
            d = float(input('Digite o deslocamento em metros (m): '))
            t = float(input('Digite o tempo em horas (h): '))
            vm = d / (t * 3600)
            print(f'Sua velocidade média é de {vm:.2f} m/s')
            break
        elif opcao_de_transformacao == 3:
            d = float(input('Digite o descolamento em quilômetros (km): '))
            t = float(input('Digite o tempo em horas (h): '))
            vm = (d / t) / 3.6
            print(f'Sua velocidade média é de {vm:.2f} m/s')
            break
        elif opcao_de_transformacao == 0:
            d = float(input('Digite o descolamento em metros (m): '))
            t = float(input('Digite o tempo em segundos (s): '))
            vm = d / t
            print(f'Sua velocidade média é de {vm:.2f} m/s')
            break


# -----VELOCIDADE MEDIA EM KM/H------

def km_VelocidadeMedia_metros_por_hora():
    d = float(input('Digite o deslocamento em metros (m): '))
    t = float(input('Digite o tempo em horas (h): '))
    vm = (d / 1000) / t
    print(f'Sua velocidade média é de {vm:.2f} km/h')


def km_VelocidadeMedia_km_por_segundo():
    d = float(input('Digite o deslocamento em quilômetros (km): '))
    t = float(input('Digite o tempo em segundos (s): '))
    vm = d / (t / 3600)
    print(f'Sua velocidade média é de {vm:.2f} km/h')


def km_VelocidadeMedia_metros_por_segundo():
    d = float(input('Digite o descolamento em metros (m): '))
    t = float(input('Digite o tempo em segundos (s): '))
    vm = (d / t) * 3.6
    print(f'Sua velocidade média é de {vm:.2f} km/h')


def km_VelocidadeMedia_km_por_hora():
    d = float(input('Digite o descolamento em quilômetros (km): '))
    t = float(input('Digite o tempo em horas (h): '))
    vm = d / t
    print(f'Sua velocidade média é de {vm:.2f} km/h')


def km_VelocidadeMedia_Painel_Tranformacao_de_Unidade():
    while True:
        print('Desculpe não entendi, pode repetir?')
        print('''Deseja transformar alguma unidade?
                  [ 1 ] Metros (m) para quilômetros (km)
                  [ 2 ] Segundos (s) para horas (h)
                  [ 3 ] Metros (m) e segundos (s) para quilômetros (km) e horas (h)
                  [ 4 ] Não desejo''')
        opcao_de_transformacao = int(input('Qual a sua opção? '))
        if opcao_de_transformacao == 1:
            d = float(input('Digite o deslocamento em metros (m): '))
            t = float(input('Digite o tempo em horas (h): '))
            vm = (d / 1000) / t
            print(f'Sua velocidade média é de {vm:.2f} km/h')
            break
        elif opcao_de_transformacao == 2:
            d = float(input('Digite o deslocamento em quilômetros (km): '))
            t = float(input('Digite o tempo em segundos (s): '))
            vm = d / (t / 3600)
            print(f'Sua velocidade média é de {vm:.2f} km/h')
            break
        elif opcao_de_transformacao == 3:
            d = float(input('Digite o descolamento em metros (m): '))
            t = float(input('Digite o tempo em segundos (s): '))
            vm = (d / t) * 3.6
            print(f'Sua velocidade média é de {vm:.2f} km/h')
            break
        elif opcao_de_transformacao == 4:
            d = float(input('Digite o descolamento em quilômetros (km): '))
            t = float(input('Digite o tempo em horas (h): '))
            vm = d / t
            print(f'Sua velocidade média é de {vm:.2f} km/h')
            break


# -----DESLOCAMENTO EM METROS------

def metros_Deslocamento_km_por_hora_por_segundo():
    vm = float(input('Digite sua velocidade média em quilômetros (km/h): '))
    t = float(input('Digite o tempo em segundos (s): '))
    d = (vm / 3.6) * t
    print(f'O deslocamento foi de {d:.2f}m')


def metros_Deslocamento_metros_por_segundo_por_hora():
    vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
    t = float(input('Digite seu tempo em horas (h): '))
    d = vm * (t * 3600)
    print(f'O deslocamento foi de {d:.2f}m')


def metros_Deslocamento_km_por_hora_por_hora():
    vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
    t = float(input('Digite seu tempo em horas (h): '))
    d = (vm * t) * 1000
    print(f'O deslocamento foi de {d:.2f}m')


def metros_Deslocamento_metros_por_segundo_por_segundo():
    vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
    t = float(input('Digite seu tempo em segundos (s): '))
    d = vm * t
    print(f'Seu deslocamento foi de {d:.2f}m')


def metros_Deslocamento_Painel_Tranformacao_de_Unidade():
    while True:
        print('Desculpe não entendi, pode repetir?')
        print(''' Deseja transformar alguma unidade? 
                    [ 1 ] Quilômetros por hora (km/h) para metros por segundo (m/s)
                    [ 2 ] Horas (h) para segundos (s)
                    [ 3 ] Quilômetros por hora (km/h) e horas (h) para metros por segundo (m/s) e segundos (s)
                    [ 0 ] Não desejo''')
        opcao_de_transformacao = int(input("Qual sua opção? "))
        if opcao_de_transformacao == 1:
            vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
            t = float(input('Digite o tempo em segundos (s): '))
            d = (vm / 3.6) * t
            print(f'O deslocamento foi de {d:.2f}m')
            break
        elif opcao_de_transformacao == 2:
            vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
            t = float(input('Digite seu tempo em horas (h): '))
            d = vm * (t * 3600)
            print(f'O deslocamento foi de {d:.2f}m')
            break
        elif opcao_de_transformacao == 3:
            vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
            t = float(input('Digite seu tempo em horas (h): '))
            d = (vm * t) * 1000
            print(f'O deslocamento foi de {d:.2f}m')
            break
        elif opcao_de_transformacao == 0:
            vm = float(input('Digite sua velocidade media em metros por segundo (m/s): '))
            t = float(input('Digite seu tempo em segundos (s): '))
            d = vm * t
            print(f'Seu deslocamento foi de {d:.2f}m')
            break


# -----DESLOCAMENTO EM KM------
def km_Deslocamento_metros_por_segundos_por_hora():
    vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
    t = float(input('Digite o tempo em horas (h): '))
    d = (vm * 3.6) * t
    print(f'O deslocamento foi de {d:.2f}km')


def km_Deslocamento_km_por_hora_por_segundo():
    vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
    t = float(input('Digite seu tempo em segundos (s): '))
    d = vm * (t / 3600)
    print(f'O deslocamento foi de {d:.2f}km')


def km_Deslocamento_metros_por_segundo_por_segundo():
    vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
    t = float(input('Digite seu tempo em segundos (s): '))
    d = (vm * t) / 1000
    print(f'O deslocamento foi de {d:.2f}km')


def km_Deslocamento_km_por_hora_por_hora():
    vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
    t = float(input('Digite seu tempo em horas (h): '))
    d = vm * t
    print(f'Seu deslocamento foi de {d:.2f}km')


def km_Deslocamento_Painel_Tranformacao_de_unidade():
    while True:
        print('Desculpe não entendi, pode repetir?')
        print(''' Deseja transformar alguma unidade? 
                    [ 1 ] Metros por segundo (m/s) para quilômetros por hora (km/h)
                    [ 2 ] Segundos (s) para horas (h)
                    [ 3 ] Metros por segundo (m/s) e segundos (s) para quilômetros por hora (km/h) e horas (h)
                    [ 4 ] Não desejo''')
        opcao_de_transformacao = int(input("Qual sua opção? "))
        if opcao_de_transformacao == 1:
            vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
            t = float(input('Digite o tempo em horas (h): '))
            d = (vm * 3.6) * t
            print(f'O deslocamento foi de {d:.2f}km')
            break
        elif opcao_de_transformacao == 2:
            vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
            t = float(input('Digite seu tempo em segundos (s): '))
            d = vm * (t / 3600)
            print(f'O deslocamento foi de {d:.2f}km')
            break
        elif opcao_de_transformacao == 3:
            vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
            t = float(input('Digite seu tempo em segundos (s): '))
            d = (vm * t) / 1000
            print(f'O deslocamento foi de {d:.2f}km')
        elif opcao_de_transformacao == 4:
            vm = float(input('Digite sua velocidade media em quilômetros por hora (km/h): '))
            t = float(input('Digite seu tempo em horas (h): '))
            d = vm * t
        print(f'Seu deslocamento foi de {d:.2f}km')
        break


# -----TEMPO EM SEGUNDOS------
def segundos_Tempo_km_por_hora_por_metros():
    vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
    d = float(input('Digite seu deslocamento em metros (m): '))
    t = d / (vm / 3.6)
    print(f'Seu tempo é de {t:.2f}s')


def segundos_Tempo_metros_por_segundo_por_km():
    vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
    d = float(input('Digite seu deslocamento em quilômetros (km): '))
    t = (d * 1000) / vm
    print(f'Seu tempo é de {t:.2f}s')


def segundos_Tempo_km_por_hora_por_km():
    vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
    d = float(input('Digite seu deslocamento em quilômetros (km): '))
    t = (d / vm) * 3600
    print(f'Seu tempo é de {t:.2f}s')


def segundos_Tempo_metros_por_segundo_por_metros():
    vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
    d = float(input('Digite seu deslocamento em metros (m): '))
    t = d / vm
    print(f'Seu tempo é de {t:.2f}s')


def segundos_Tempo_Painel_Transformacao_de_Unidade():
    while True:
        print('Desculpe não entendi, pode repetir?')
        print(''' Deseja transformar alguma unidade? 
                    [ 1 ] Quilômetros por hora (km/h) para metros por segundo (m/s)
                    [ 2 ] Quilômetros (km) para metros (m)
                    [ 3 ] Quilômetros por hora (km/h) e horas (h) para metros por segundo (m/s) e segundos (s)
                    [ 0 ] Não desejo''')
        opcao_de_transformacao = int(input("Qual sua opção? "))
        if opcao_de_transformacao == 1:
            vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
            d = float(input('Digite seu deslocamento em metros (m): '))
            t = d / (vm / 3.6)
            print(f'Seu tempo é de {t:.2f}s')
            break
        elif opcao_de_transformacao == 2:
            vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
            d = float(input('Digite seu deslocamento em quilômetros (km): '))
            t = (d * 1000) / vm
            print(f'Seu tempo é de {t:.2f}s')
            break
        elif opcao_de_transformacao == 3:
            vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
            d = float(input('Digite seu deslocamento em quilômetros (km): '))
            t = (d / vm) * 3600
            print(f'Seu tempo é de {t:.2f}s')
            break
        elif opcao_de_transformacao == 0:
            vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
            d = float(input('Digite seu deslocamento em metros (m): '))
            t = d / vm
            print(f'Seu tempo é de {t:.2f}s')
            break


# -----TEMPO EM HORAS------
def horas_Tempo_metros_por_segundo_por_km():
    vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
    d = float(input('Digite seu deslocamento em quilômetros (km): '))
    t = d / (vm * 3.6)
    print(f'Seu tempo é de {t:.2f}h')


def horas_Tempo_km_por_hora_por_metros():
    vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
    d = float(input('Digite seu deslocamento em metros (m): '))
    t = (d / 1000) / vm
    print(f'Seu tempo é de {t:.2f}h')


def horas_Tempo_metros_por_segundo_por_metros():
    vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
    d = float(input('Digite seu deslocamento em metros (m): '))
    t = (d / vm) / 3600
    print(f'Seu tempo é de {t:.2f}h')


def horas_Tempo_km_por_hora_por_km():
    vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
    d = float(input('Digite seu deslocamento em quilômetros (km): '))
    t = d / vm
    print(f'Seu tempo é de {t:.2f}h')


def hora_Tempo_Painel_Transformacao_de_Unidade():
    while True:
        print('Desculpe não entendi, pode repetir?')
        print(''' Deseja transformar alguma unidade? 
                    [ 1 ] Metros por segundo (m/s) para quilômetros por hora (km/h)
                    [ 2 ] Metros (m) para quilômetros (km)
                    [ 3 ] Metros por segundo (m/s) e segundos (s) para quilômetros por hora (km/h) e horas (h)
                    [ 0 ] Não desejo''')
        opcao_de_transformacao = int(input("Qual sua opção? "))
        if opcao_de_transformacao == 1:
            vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
            d = float(input('Digite seu deslocamento em quilômetros (km): '))
            t = d / (vm * 3.6)
            print(f'Seu tempo é de {t:.2f}h')
            break
        elif opcao_de_transformacao == 2:
            vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
            d = float(input('Digite seu deslocamento em metros (m): '))
            t = (d / 1000) / vm
            print(f'Seu tempo é de {t:.2f}h')
            break
        elif opcao_de_transformacao == 3:
            vm = float(input('Digite sua velocidade média em metros por segundo (m/s): '))
            d = float(input('Digite seu deslocamento em metros (m): '))
            t = (d / vm) / 3600
            print(f'Seu tempo é de {t:.2f}h')
            break
        elif opcao_de_transformacao == 0:
            vm = float(input('Digite sua velocidade média em quilômetros por hora (km/h): '))
            d = float(input('Digite seu deslocamento em quilômetros (km): '))
            t = d / vm
            print(f'Seu tempo é de {t:.2f}h')
            break
