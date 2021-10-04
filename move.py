import pygame
from text import print_text_pygame
import test

# size_of_screen 	= (1280, 800)
size_of_screen 	= (1900, 1080)
# size_of_screen 	= (1000, 700)
W, H, FPS		= *size_of_screen, 120
WHITE			= (255, 255, 255)
BNT_IN 			= (0, 0, 0)
BNT_OUT 		= (255, 0, 0)
level        	= 1
W_car = 200
H_car = 150
line = test.Map()
pygame.init()

sc          = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
clock       = pygame.time.Clock()
    
def button(x, y, w, h, txt, txt_size, txt_color, x_sh, y_sh, func, photo=False):
    '''здесь создается нажатие на кнопки и их взаимодеиствия '''
    mouse 		= pygame.mouse.get_pos()
    is_clicked  = pygame.mouse.get_pressed() 
    if x - w // 2 < mouse[0] < x + w // 2 and y - w // 2 < mouse[1] < y + h // 2:
        if photo:
            x_b, y_b = x - photo[1][1] // 2, y - photo[1][2] // 2
            sc.blit(photo[1][0], (x_b, y_b))
        else:
            pygame.draw.rect(sc, BNT_IN, (x - w // 2, y - h //2, w, h))
            print_text_pygame(txt, txt_size, sc, (x, y), BNT_OUT)
        if is_clicked[0]:
            pygame.time.delay(300)
            if func is None:
                return True
            else:
                return func()
    else:
        if photo:
            sc.blit(photo[0][0], (x - photo[0][1] // 2, y - photo[0][2] // 2))
        else:
            pygame.draw.rect(sc, BNT_OUT, (x - w // 2, y - h // 2, w, h))
            print_text_pygame(txt, txt_size, sc, (x, y), BNT_IN)
        
        
        
def move_for_game():           
    bomb    = pygame.image.load('/Users/matveybazhanov/Desktop/play_111/bomb.png')
    bombs   = [[pygame.transform.scale(bomb, (100, 100)), 100, 100]]
    bombs.append([pygame.transform.scale(bomb, (150, 150)), 150, 150])
    
    for_bomb    = pygame.image.load('/Users/matveybazhanov/Desktop/play_111/for_bomb.png')
    for_bombs   = [[pygame.transform.scale(for_bomb, (100, 100)), 100, 100]]
    for_bombs.append([pygame.transform.scale(for_bomb, (150, 150)), 150, 150])
    
    fire    = pygame.image.load('/Users/matveybazhanov/Desktop/play_111/fire.png')
    fires   = [[pygame.transform.scale(fire, (100, 100)), 100, 100]]
    fires.append([pygame.transform.scale(fire, (150, 150)), 150, 150])
    
    info    = pygame.image.load('/Users/matveybazhanov/Desktop/play_111/info.png')
    infos   = [[pygame.transform.scale(info, (100, 100)), 100, 100]]
    infos.append([pygame.transform.scale(info, (150, 150)), 150, 150])
    
    forest    = pygame.image.load('/Users/matveybazhanov/Desktop/play_111/forest.png')
    forests   = [[pygame.transform.scale(forest, (100, 100)), 100, 100]]
    forests.append([pygame.transform.scale(forest, (150, 150)), 150, 150])
    
    forest    = pygame.image.load('/Users/matveybazhanov/Desktop/play_111/forest.png')
    forests   = [[pygame.transform.scale(forest, (100, 100)), 100, 100]]
    forests.append([pygame.transform.scale(forest, (150, 150)), 150, 150])
        
        
    index, flag, eco           = 0, 0, 90
    # print_text_pygame(f"level: {level}", 5, sc, (W - W // 10, H // 10), (0, 0, 0))
    print_text_pygame(f"Eco: {eco}", 5, sc, (W - W // 10 - 500, H // 10), (0, 0, 0))
    # button(W - W // 10 - 400, H // 10 + 200, 200, 100, f'{index, city}', 3, (0 ,0, 0,), 50, 30, Russia, None)
    # if button(W - W // 10 - 400, H // 10 + 200, 200, 100, f'{index, city}', 3, (0 ,0, 0,), 50, 30, None, None):
    #    city += 1
    #    if city > 4:
    #        index += 1
    #        city = 0 

    if button(W // 2, H // 8 * 7, 200, 100, f'{index}', 5, (0, 0, 0), 30, 30, None, None):
        pass
        # level_for_play  = False
    
    
        
    '''закупка ядерных бомб'''
    # if button(W - W // 10, H // 8 * 7 - 200, 200, 100, '', 5, (0, 0, 0), 30, 30, Ru, for_bombs):  
    #     # test.table.loc['Russia'].money[city] -= 500
    #     Ru()
        
        # if test.table.loc['Russia'].bomb[index] is False:
            # if test.table.loc['Russia'].money[index] >= 500:
                # eco -= 3
                # test.table.loc['Russia'].bomb[index] = True
    
    # if button(W - W // 10, H // 8 * 7 - 1000, 200, 100, '', 5, (0, 0, 0), 30, 30, None, for_bombs):
    #     test.change_value(test.table, 'Ru', 'Moscow', 'money', +100)
        
        
        
        
        # if money[flag] >= 300:
        #     money[flag] -= 300
        #     shield[flag] = True

    if button(W - W // 10 , H // 8 * 7, 200, 100, '', 5, (0 ,0, 0,), 50, 30, None, forests):  
        pass
        # if money[flag] >= 200:
            # money[flag] -= 200
            # eco += 14 
    
    if button(W - W // 10 , H // 8 * 7 - 400, 200, 100, '', 5, (0 ,0, 0,), 50, 30, None, bombs):  
        pass
        # if bomb_333 is True:    
        #     if money[flag] >= 150:
        #         money[flag] -= 150
        #         eco += 3
        #         shoot[flag] += 1
    
    # # улучшение города 
    # if button(W - W // 10 , H // 8 * 7 - 600, 200, 100, '', 5, (0 ,0, 0,), 50, 30, None, infos):  
    #     if money[flag] >= 150:
    #         money[flag] -= 150        
    #         development_dddd[flag] += 20
            
    # if button(W - W // 10 , H // 8 * 7 - 800, 200, 100, '', 5, (0 ,0, 0,), 50, 30, None, fires):
    #     if shoot[flag] == 0:
    #         shoot[flag] = 0
    #     else:
    #         if shield[flag] is False:
    #             shoot[flag] -= 1
    #             eco -= 3
                
                
    #         else:
    #             shield[flag] = False

    # if level_for_play is False:
    #     if flag >= 5:
    #         flag = -1
    #         level += 1
    #     else:
    #         money_city_1[flag] = int(300 * development_dddd[flag] // 100)
    #         # money_city_2[flag] = int(300 * development_ddd[flag] // 100)
    #         # money_city_3[flag] = int(300 * development_dd[flag] // 100)
    #         # money_city_4[flag] = int(300 * development_d[flag] // 100)
    #         flag += 1
    #         level_for_play = True
    pygame.display.update()