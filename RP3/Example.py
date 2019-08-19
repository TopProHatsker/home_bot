import RPi.GPIO as GPIO                 # Импортируем библиотеку по работе с GPIO
import time                             # Импортируем класс для работы со временем

try:
    # === Инициализация пинов ===
    #pin=5
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(pin, GPIO.OUT, initial=1)

    # Здесь размещаем основной рабочий код
    # ...

except KeyboardInterrupt:
    # ...
    print("Exit pressed Ctrl+C")        # Выход из программы по нажатию Ctrl+C
except:
    # ...
    print("Other Exception")            # Прочие исключения
finally:
    GPIO.cleanup()                      # Возвращаем пины в исходное состояние
    print("End of program")             # Информируем о завершении работы программы
