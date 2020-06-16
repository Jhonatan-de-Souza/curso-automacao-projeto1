import random
import schedule


def EnviarAlerta():
    sugestoes = ['Ligue', 'Desligue', 'continuar']
    print(random.choice(sugestoes))


schedule.every(5).seconds.do(EnviarAlerta)

while True:
    schedule.run_pending()
