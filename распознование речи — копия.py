import keyboard
import speech_recognition as sr


import pywhatkit as kit

# Номер получателя и сообщение
sergay = '+79670331777'
timofey='+79268403751'

message = '' 

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print('ГОВОРИ')
        r.pause_threshold = 1  # Исправлено название переменной
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="ru-RU").lower()
    except sr.UnknownValueError:
        #print("Не удалось распознать речь")
        text = ""
    except sr.RequestError as e:
        print(f"Ошибка сервиса Google Speech Recognition: {e}")
        text = ""
    return text

a = ''
recording = False

while True:
    text = listen()
    #print(text)
    '''if 'отправить' in text:
            keyboard.press('enter')

            keyboard.release('enter')'''
    if 'начать запись' in text:
        recording = True
        a = ''
        print("Запись началась...")
    
    while recording:
        text = listen()
        #print(text)
        if 'остановить запись' in text:
            recording = False
            print("Запись остановлена.")
        elif 'отправить' in text:
            #keyboard.write(a)
            keyboard.press('enter')
            keyboard.release('enter')
            a = ''
        elif 'отправить сообщение' in text:
            message = text
            kit.sendwhatmsg_instantly(phone_number, message)
        elif 'очистить' in text:
            keyboard.send('ctrl+a')
            keyboard.send('backspace')
        elif 'удалить слово' in text:
            keyboard.send('ctrl+a+backspace')
        elif 'стоп' in text:
             break
        else:
            a += text + ' '
            keyboard.write(text + ' ')
        
    if 'отправить сообщение сергей' in text:
        message = text
        message=message.replace('отправить сообщение сергей', '')
        kit.sendwhatmsg_instantly(sergay, message)
    if 'отправить сообщение тимофей' in text:


        message = text
        message=message.replace('отправить сообщение тимофей', '')
        kit.sendwhatmsg_instantly(timofey, message)
    if 'очистить' in text:
        keyboard.send('ctrl+a')
        keyboard.send('backspace')
    if 'удалить слово' in text:
        keyboard.send('ctrl+a+backspace')
    if 'закрыть приложение' in text:
        keyboard.send('alt+f4')
    if 'следующая вкладка' in text:
        keyboard.send('alt+tab')
    if 'отправить' in text:
        keyboard.send('enter')
    if 'стоп' in text:
        break




    
