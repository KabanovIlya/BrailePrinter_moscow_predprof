#BCode text slicer v1.1
#теперь распознает голос
#Символ точки - "."
#Символ пробела(пропуска) - "-"
#Символ новой строки - "*"
#особенности
#можно добавить свои символы
#преобразует любой текст из русских символов
#не поддерживает спецзнаки(можно добавить)
#Сделал Илья Кабанов
from time import sleep
import serial
import queue
import sys
import sounddevice as sd
from vosk import Model, KaldiRecognizer
#variables
q = queue.Queue()
text_a = []
buffer = []
text = ''
stop = False
textappend = ''
generated_bcode = []
current_string_mass = []
text_mass = []
current_in_symb = 1
current_string = 1
strings = 0
init = 0
letters_on_one_string = 12 #Букв в одной строке
def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))
dev_id=1 # 9 или 39
lang='ru'
device_info = sd.query_devices(dev_id, "input")
samplerate = int(device_info["default_samplerate"])
model = Model('vosk-model-small-ru')
#dictonary
a = {1:['.','-'],
     2:['-','-'],
     3:['-','-']}

b = {1:['.','-'],
     2:['.','-'],
     3:['-','-']}

v = {1:['-','.'],
     2:['.','.'],
     3:['-','.']}

g = {1:['.','.'],
     2:['.','.'],
     3:['-','-']}

d = {1:['.','.'],
     2:['-','.'],
     3:['-','-']}

e = {1:['.','-'],
     2:['-','.'],
     3:['-','-']}

yo = {1:['.','-'],
     2:['-','-'],
     3:['-','.']}

j = {1:['-','.'],
     2:['.','.'],
     3:['-','-']}

z = {1:['.','-'],
     2:['-','.'],
     3:['.','.']}

ai = {1:['-','.'],
     2:['.','-'],
     3:['-','-']}

y = {1:['.','.'],
     2:['.','-'],
     3:['.','.']}

k = {1:['.','-'],
     2:['-','-'],
     3:['.','-']}

l = {1:['.','-'],
     2:['.','-'],
     3:['.','-']}

m = {1:['.','.'],
     2:['-','-'],
     3:['.','-']}

n = {1:['.','.'],
     2:['-','.'],
     3:['.','-']}

o = {1:['.','-'],
     2:['-','.'],
     3:['.','-']}

p = {1:['.','.'],
     2:['.','-'],
     3:['.','-']}

r = {1:['.','-'],
     2:['.','.'],
     3:['.','-']}

s = {1:['-','.'],
     2:['.','-'],
     3:['.','-']}

t = {1:['-','.'],
     2:['.','.'],
     3:['.','-']}

u = {1:['.','-'],
     2:['-','-'],
     3:['.','.']}

f = {1:['.','.'],
     2:['.','-'],
     3:['-','-']}

x = {1:['.','-'],
     2:['.','.'],
     3:['-','-']}

ts = {1:['.','.'],
     2:['-','-'],
     3:['-','-']}

ch = {1:['.','.'],
     2:['.','.'],
     3:['.','-']}

sh = {1:['.','-'],
     2:['-','.'],
     3:['-','.']}

sbh = {1:['.','.'],
     2:['-','-'],
     3:['.','.']}

tvz = {1:['.','-'],
     2:['.','.'],
     3:['.','.']}

yi = {1:['-','.'],
     2:['.','-'],
     3:['.','.']}

mz = {1:['-','.'],
      2:['.','.'],
     3:['.','.']}

ee = {1:['-','.'],
     2:['.','-'],
     3:['-','.']}

yu = {1:['.','-'],
     2:['.','.'],
     3:['-','.']}

ya = {1:['.','.'],
     2:['.','-'],
     3:['-','.']}

#generator
while True:
    with (sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=dev_id,dtype="int16", channels=1, callback=callback)):
        print("#" * 80)
        print("Идет запись! Ctrl+C для остановки программы")
        print("#" * 80)
        rec = KaldiRecognizer(model, samplerate)
        while True:
            text_a = []
            data = q.get()
            if rec.AcceptWaveform(data):
               textappend = rec.Result()[14:]
               textappend = textappend[:-3]
               text_a.append(textappend.split())
               print(text_a)
               try:
                    if text_a[0][0]== "распечатать":
                        text_a[0].pop(0)
                        print('Текст успешно получен!',text_a)
                        break
               except:
                   print('Произошла ошибка, пробуем получить текст еще раз...')
    if text_a[0][0]=='стоп':
        stop=True
    for jmm in text_a[0]:
        text = text + jmm + ' '
    for kk in text:
        text_mass.append(kk)
    print('получен текст', text)
    print(stop)
    if stop == False:
        while len(text_mass) > 0:
            if len(text_mass)<letters_on_one_string:
                for xx in range(len(text_mass)):
                    current_string_mass.append(text_mass[0])
                    text_mass.pop(0)
            else:
                for xx in range(letters_on_one_string):
                    current_string_mass.append(text_mass[0])
                    text_mass.pop(0)
            for uu in range(3):
                for zz in current_string_mass:
                    if zz == 'а' or zz == 'А':
                        for i in a[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'б' or zz == 'Б':
                        for i in b[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'в' or zz == 'В':
                        for i in v[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'г' or zz == 'Г':
                        for i in g[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'д' or zz == 'Д':
                        for i in d[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'е' or zz == 'Е':
                        for i in e[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ё' or zz == 'Ё':
                        for i in yo[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ж' or zz == 'Ж':
                        for i in j[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'з' or zz == 'З':
                        for i in z[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'и' or zz == 'И':
                        for i in ai[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'й' or zz == 'Й':
                        for i in y[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'к' or zz == 'К':
                        for i in k[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'л' or zz == 'Л':
                        for i in l[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'м' or zz == 'М':
                        for i in m[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'н' or zz == 'Н':
                        for i in n[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'о' or zz == 'О':
                        for i in o[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'п' or zz == 'П':
                        for i in p[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'р' or zz == 'Р':
                        for i in r[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'с' or zz == 'С':
                        for i in s[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'т' or zz == 'Т':
                        for i in t[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'у' or zz == 'У':
                        for i in u[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ф' or zz == 'Ф':
                        for i in f[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'х' or zz == 'Х':
                        for i in x[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ц' or zz == 'Ц':
                        for i in ts[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ч' or zz == 'Ч':
                        for i in ch[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ъ' or zz == 'Ъ':
                        for i in tvz[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ы' or zz == 'Ы':
                        for i in yi[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'э' or zz == 'Э':
                        for i in ee[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ю' or zz == 'Ю':
                        for i in yu[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'я' or zz == 'Я':
                        for i in ya[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ь' or zz == 'Ь':
                        for i in mz[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'ш' or zz == 'Ш':
                        for i in sh[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == 'щ' or zz == 'Щ':
                        for i in sbh[current_in_symb]:
                            generated_bcode.append(i)
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                    if zz == " ":
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                        generated_bcode.append('-')
                generated_bcode.append('*')
                current_in_symb +=1;
                print(current_in_symb)
            current_in_symb = 1
            current_string_mass = []
            generated_bcode.append('*')
            generated_bcode.append('*')
    elif stop == True:
        generated_bcode.append('/')
        stop=False
    print(generated_bcode)
    print("BCode успешно сгенерирован!")
    if init == 0:
        init = 1
        ser = serial.Serial("COM5", 9600)
        print("Ожидание инициализации принтера")
        sleep(8)
        print("Время ожидания истекло, начинаю печать")
    for qq in generated_bcode:
        if qq=='/':
            abobusjmix = 'gohome\n'
            ser.write(abobusjmix.encode())
        qqa = qq+"\n"
        ser.write(qqa.encode())
        sleep(0.8)
    print('Печать завершена!')
    sleep(1)
    generated_bcode = []
    text = ""