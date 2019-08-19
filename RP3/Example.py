
# import RPi.GPIO as GPIO                 # Импортируем библиотеку по работе с GPIO
import time  # Импортируем класс для работы со временем


class RaspberryPi3B:

    def __init__(self, Pump_PIN, Wet_PIN, MinWet):
        self.Pump_PIN = Pump_PIN
        self.Wet_PIN = Wet_PIN
        self.MinWet = MinWet
        self.RealWet = 0
        self.AutoMode = False

    def auto_mode(self):
        pass

    def manual_watering(self):
        # поливает
        pass

    def get_info(self):
        return  self.AutoMode, self.MinWet, self.RealWet


"""
try:
    # === Инициализация пинов ===
    # pin=5
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(pin, GPIO.OUT, initial=1)

    # Здесь размещаем основной рабочий код
    # ...
    pass

except KeyboardInterrupt:
    print("Exit pressed Ctrl+C")  # Выход из программы по нажатию Ctrl+C
except:
    print("Other Exception")  # Прочие исключения
finally:
    # GPIO.cleanup()                      # Возвращаем пины в исходное состояние
    print("End of program")  # Информируем о завершении работы программы
"""