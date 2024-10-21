import time
from zapv2 import ZAPv2

zap = ZAPv2(apikey='api_key', proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

target = 'http://google.com'

print(f"Iniciando spider em {target}")
zap.spider.scan(target)
time.sleep(2)

while int(zap.spider.status()) < 100:
    print(f"Spider em andamento: {zap.spider.status()}%")
    time.sleep(2)

print("Spider completo. Iniciando varredura ativa.")

zap.ascan.scan(target)

while int(zap.ascan.status()) < 100:
    print(f"Varredura em andamento: {zap.ascan.status()}%")
    time.sleep(5)

print("Varredura completa. Obtendo resultados.")

alerts = zap.core.alerts(baseurl=target)

for alert in alerts:
    print(f"Alerta: {alert['alert']}")
    print(f"Descrição: {alert['description']}")
    print(f"Gravidade: {alert['risk']}")
    print(f"Recomendação: {alert['solution']}\n")
