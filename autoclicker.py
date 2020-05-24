import os
import mouse as m
import keyboard as k
import time

def clear ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
	print('''
  ▐▄▄▄       ▄ .▄ ▐ ▄ 
 ▪·██ ▄█▀▄ ██▪▐█•█▌▐█
▪▄ ██▐█▌.▐▌██▀▀█▐█▐▐▌
▐▌▐█▌▐█▌.▐▌██▌▐▀██▐█▌
 ▀▀▀• ▀█▄▀▪▀▀▀ ·▀▀ █▪
	''')

clear ()
main()


try:
	click = input('Введите количество кликов: ')
	c = click.replace(',', '.').split()
	cclick = float(c[0])
	my_time = input('Введите задержку между кликами(в секундах): ')
	t = my_time.replace(',', '.').split()
	mytime = float(t[0])
except ValueError:
	print('Вы ввели не число!')
	time.sleep(3)
	quit()

start = input('Выберите кнопку включения: ')
stop = input('Выберите кнопку выключения: ')


i = 0
def clicker():
	global i
	while i < cclick:
		time.sleep(mytime)
		m.click(button ='left')
		i += 1
		
		if i == cclick:
			quit()	
		elif k.is_pressed(stop):
			quit()

while True:
	if k.is_pressed(start):
		clicker()
