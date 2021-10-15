import random
from typing import Counter
import numpy as np
import pandas as pd
import pygame as pg
from text import print_text_pygame
import os
development            = [100, 80, 60, 20]
W, H 	= 1900, 1080

columns = 'country', 'city', 'money', 'shoot', 'shield', 'development'
data = {
    'Ru':{
        'Moscow':           [1500, 0, False, development[0]],
        'Saint-Petersburg': [1000, 0, False, development[1]],
        'Chelyabinsk':      [100, 0, True, development[2]],
        'Vologda':          [150, 0, False, development[3]]
    },
    'Chi': {
        'Beijing':          [1500, 0, False, development[0]],
        'Shanghai':         [1000, 0, False, development[1]],
        'Wuhan':            [100, 0, True, development[2]],
        'Nanjing':          [150, 0, False, development[3]]
                                    
    },
    
    'Ja':{
        'Tokyo':        [1000, 0, False, development[1]],
        'Kyota':        [1000, 0, False, development[1]],
        'Hiroshima':    [1000, 0, False, development[1]],
        'Nagasaki':     [1000, 0, False, development[1]]     
    },
    
    'USA': {
        'Washington':       [1000, 0, False, development[1]],
        'New-York':         [1000, 0, False, development[1]],
        'Chicago':          [1000, 0, False, development[1]],
        'Los-Angeles':      [1000, 0, False, development[1]]
    },
   
    
    'It': {
    'Rome':             [1000, 0, False, development[1]],
    'Venice':           [1000, 0, False, development[1]],
    'Milan':            [1000, 0, False, development[1]],
    'Turin':            [1000, 0, False, development[1]]
    },
    
    'Uk': {
    'Kiev':            [1000, 0, False, development[1]],
    'Odessa':          [1000, 0, False, development[1]],
    'Donetsk':         [1000, 0, False, development[1]],
    'Luhansk':         [1000, 0, False, development[1]]
    },
    
}
       


# table = pd.DataFrame([[k, v] + data[k][v] for k, values in data.items() for v in values])
# table.columns = columns
list_result = []
for country, contry_data in data.items():
    for city in contry_data:
        data_item = [country, city] + data[country][city]
        list_result.append(data_item)

table = pd.DataFrame(list_result, columns=columns)


pic_country = [
    pg.image.load('assets/Russia.png'),
    pg.image.load('assets/China.png'),
    pg.image.load('assets/Japan.png'),
    pg.image.load('assets/USA.png'), 
    pg.image.load('assets/Ukrain.png')]

# for i in  pic_coutry: 
#     hfbdj
#     pic_country = pg.transform.scale(pic_country[0], (50, 50))
for column in ['money', 'shoot', 'development']:
    table.loc[:, column] = table[column].astype(int)


def set_value(country, city, column, value, df=table):
    df.loc[(df.country == city) & (df.city == city), column] = value
    return df

def change_value(df, country, city, column, value):
    df.loc[(df.country == country) & (df.city == city), column] += value
    return df
print(table.loc[0, 0].money - 100)

def draw_dataframe(sc, data=table, x=W // 8, y=100):
    data_str = data.iloc[:, 1:].to_string()
    step = 40
    y_index = y
    country_index = 0 
    for i, element in enumerate(data_str.split('\n')):
        amount_space = element.index(' ')
        output_string = ' ' * amount_space + element[amount_space:]
        
        print_text_pygame(output_string, 1, sc, (x + 30, y_index), (0, 0, 0))  
        y_index += step
        
        if (y_index - y) % (step * 4) == 0:
            sc.blit(pic_country[country_index], (x - 250, y_index - 2 * step))
            if country_index == 4:
                country_index = 0 
            else:
                country_index += 1


# end_string = '\n' + '#' * 70 + '\n'
# print(table, end=end_string)
# print(table.query("country == 'Ru'"), end=end_string)
# print(table.query("country == 'Ru' and city == 'Moscow'"), end=end_string)

# table = set_value('Ru', 'Moscow', 'money', 1234567)
# table = change_value('Ru', 'Moscow', 'money', -100)

# print(table.query("country == 'Ru' and city == 'Moscow'"), end=end_string)



class Map:
    def __init__(self):
        self.w = 6
        self.h = 9
        self.width_size = 19
        self.height_size = 10
        self.size_w = self.width_size // self.w
        self.size_h = self.height_size // self.h
        self.cur_cell = None

    def draw(self, win):
        # вертикальные линии 
        y_index = H // 3
        for line in range(self.w + 1):
            pg.draw.line(win, (0, 0, 0), (line * self.size_w, 0), (line * self.size_w, self.height_size))
        # горизонтальная линии 
        for line in range(self.h + 1):
            x = W 
            pg.draw.line(win, (0, 0, 0), (0, line * self.size_h), (self.width_size, line * self.size_h))

    
    def check_highlite_cursor(self, win):
        x, y = pg.mouse.get_pos()
        index_x, index_y = x // self.size_w, y // self.size_h
        
        if index_x < self.w and index_y < self.h:
            is_pressed = pg.mouse.get_pressed()

            x_rect = index_x * self.size_w
            y_rect = index_y * self.size_h
            pg.draw.rect(win, (255, 0, 0), (x_rect, y_rect, self.size_w, self.size_h), 3)

            if is_pressed[0] is True:
                self.cur_cell = index_x, index_y
            if self.cur_cell is not None:
                pg.draw.rect(win, (0, 255, 0), (self.cur_cell[0] * self.size_w,
                                                self.cur_cell[1] * self.size_h,
                                                self.size_w, self.size_h), 3)


#index location
# print(table.iloc[0, 4])