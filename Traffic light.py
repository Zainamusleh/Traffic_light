from gpiozero import LED
from time import sleep
ledR= LED(2)
ledY= LED(3)
ledG= LED(4)
while True:
    ledR.on()
    sleep(5)
    ledR.off()
    ledY.on()
    sleep(1)
    ledY.off()
    ledG.on()
    sleep(5)
    ledG.off()