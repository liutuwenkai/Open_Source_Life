import pygame
import sys
from pygame.locals import *

pygame.init()
# 启用python中的 pygame
pygame.joystick.init()
screen = pygame.display.set_mode((1024,768),0,0)  # 修改第一个参数为 FULLSCREEN 改为全屏
pygame.display.set_caption('Open_Source_Life')
myfont = pygame.font.SysFont("monospace", 2)
Matrix = [[(0) for x in range(96)] for x in range(128)]  # range * 8 = 分辨率
clock = pygame.time.Clock()
# Pygame.time.Clock()会控制每个循环多长时间运行一次。
# 这就像一个定时器在控制时间进程，
# 指出“现在开始下一个循环”！现在开始下一个循环
FPS = 60
playtime = 0.0
formiga = []
# forgima 蚂蚁
formiga.append(50)
formiga.append(50)
formiga.append(1)
inte=0;
joysticks = []
# 初始化（initialize）

while 1:
	background = pygame.Surface((screen.get_size()))
	background.fill((0, 0, 0))

	for i in range(0,pygame.joystick.get_count()):
		joysticks.append(pygame.joystick.Joystick(0))
		joysticks[-1].init()

	for event in pygame.event.get():
		if event.type == QUIT:
			a.close()
			pygame.quit()
			sys.exit()

		if event.type == pygame.JOYBUTTONDOWN:
			if event.button == 0 or event.button == 1 or event.button == 2 or event.button == 3 or event.button == 4 or event.button == 5  or event.button == 6 or event.button == 7 or event.button == 8:
				milliseconds = clock.tick(FPS)
				seconds = milliseconds / 1000.0
				playtime += milliseconds / 1000.0 # c += a 等效于 c = c + a

				screen.lock()

				for i in range(96):  # 坐标（i，j），未运行时预拟矩形图案
					for j in range(128):
						if Matrix[j][i] == 0:  # ==  等于 - 比较对象是否相等
							pygame.draw.rect(background, (0, 0, 255), Rect((j * 8, i * 8), (8, 8)))  # Rect 矩形
						else:
							pygame.draw.rect(background, (255, 0, 0), Rect((j * 8, i * 8), (8, 8)))

				i = 128
				while i != 0:  # !=	不等于 - 比较两个对象是否不相等
					pygame.draw.line(background, (0, 0, 255), (i * 8, 0), (i * 8, 768))  # 竖线
					i = i - 1

				i = 96
				while i != 0:
					pygame.draw.line(background, (0, 0, 255), (0, i * 8), (1024, i * 8))  # 横线
					i = i - 1

				pygame.draw.rect(background, (0, 0, 0), Rect((formiga[1] * 8, formiga[0] * 8), (8, 8)))

				if (Matrix[formiga[1]][formiga[0]] == 0 and playtime >= 0.01):
					Matrix[formiga[1]][formiga[0]] = 1
					formiga[2] = (formiga[2] + 1) % 4  # Bug 上限数 16660 百分比符号取余数
					if formiga[2] == 0:
						formiga[0] -= 1
					if formiga[2] == 1:
						formiga[1] += 1
					if formiga[2] == 2:
						formiga[0] += 1
					if formiga[2] == 3:
						formiga[1] -= 1
					pygame.draw.rect(background, (0,255, 0), Rect((formiga[1] * 8, formiga[0] * 8), (8, 8)))
					# 白转黑时显示的颜色
					playtime = 0.0
					inte += 1

				if (Matrix[formiga[1]][formiga[0]] == 1 and playtime >= 0.01):
					Matrix[formiga[1]][formiga[0]] = 0
					formiga[2] = (formiga[2] - 1) % 4
					if formiga[2] == 0:
						formiga[0] -= 1
					if formiga[2] == 1:
						formiga[1] += 1
					if formiga[2] == 2:
						formiga[0] += 1
					if formiga[2] == 3:
						formiga[1] -= 1
					pygame.draw.rect(background, (0, 255, 255), Rect((formiga[1] * 8, formiga[0] * 8), (8, 8)))
					# 黑转白时显示的颜色
					playtime = 0.0
					inte += 1
				strings = str(inte)
				label = myfont.render(strings, 1, (0, 0, 0))

				screen.unlock()
				screen.blit(background, (0, 0))
				screen.blit(label, (0, 0))
				pygame.display.update()

			# 新想法：设置一个可移动模块进行干预
