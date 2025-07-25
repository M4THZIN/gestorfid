from dialog import Dialog
import subprocess
import sys
import time

d = Dialog(dialog="dialog")

#Função que retorna o tempo restante para atualizar a tela e o tempo local para exibição no canto superior esquerdo da tela
def tempo_atual():
    agora = time.localtime()
    segundos = agora.tm_sec
    timeout = 60 - segundos #Segundos restantes para o próximo minuto
    tempo = time.strftime("%d-%m-%Y %H:%M", agora)
    d.set_background_title(f"GestorFID - {tempo}")
    return timeout

#Função principal
def menu():
    while True:
        timeout=tempo_atual()

        #Menu simples em janela com as opções
        #Timeout é definida apenas uma vez, quando a janela é criada. Se o usuário mexer na tela, o timer é resetado para 60 segundos.
        code, tag = d.menu("Escolha uma opção", title="Menu principal", choices=[
            ("1", "Leitura em tempo real"),
            ("2", "Dar baixa"),
            ("3", "Nova gravação"),
            ("4", "Banco de dados"),
            ("5", "Gerar relatório"),
            ("6", "Configurações"),
            ("7", "Sair do menu")
        ], timeout=timeout, no_cancel=True, ok_label="Aceitar")

        #Tempo acabou ou usuário apertou ESC, apenas atualiza o relógio e reapresenta o menu
        if code == d.ESC or code == d.TIMEOUT:
            continue

        #Lógica para abrir os arquivos correspondentes a escolha do usuário
        if code != d.OK or tag == "7":
            break
        if tag == "1":
            subprocess.run([sys.executable, 'leitura.py'])
        elif tag == "2":
            subprocess.run([sys.executable, 'baixa.py'])
        elif tag == "3":
            subprocess.run([sys.executable, 'gravacao.py'])
        elif tag == "4":
            subprocess.run([sys.executable, 'bancodedados.py'])
        elif tag == "5":
            subprocess.run([sys.executable, 'relatorio.py'])
        elif tag == "6":
            subprocess.run(["sudo", sys.executable, "configuracoes.py"])
            #Configuracoes.py precisa de uma autorização sudo para alterar dados internos do rasp

if __name__ == "__main__":
    menu()


