import os
from typing import Counter
import numpy as np
import pandas as pd
import pygame as pg
from text import print_text_pygame


development            = [100, 80, 60, 20]
W, H 	= 1900, 1080


country_names = [item for item in list(os.walk('assets/'))[0][-1] if item[0].isupper()]
action_names = [item for item in list(os.walk('assets/'))[0][-1] if not item[0].isupper()]

country_pics = [pg.transform.scale(pg.image.load('assets/' + item), (50, 50))\
                for item in country_names]
action_pics = [pg.transform.scale(pg.image.load('assets/' + item), (50, 50))\
                for item in action_names]

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


for column in ['money', 'shoot', 'development']:
    table.loc[:, column] = table[column].astype(int)


def set_value(country, city, column, value, df=table):
    df.loc[(df.country == country) & (df.city == city), column] = value
    return df

def change_value(df, city, column, value):
    df.loc[(df.city == city), column] += value
    return df

  
def draw_dataframe(sc, data=table, x= 0 + 350, y=0 + 50):
    data_str = data.iloc[:, 1:].to_string()
    step = 40
    y_index = y
    pic_index = 0
    
    for i, element in enumerate(data_str.split('\n')):
        amount_space = element.index(' ')
        output_string = ' ' * amount_space + element[amount_space:]
        
        print_text_pygame(output_string, 1, sc, (x + 30, y_index), (0, 0, 0))  
        y_index += step
        
        if (y_index - y) % (step * 4) == 0:
            sc.blit(country_pics[pic_index], (x - 300, y_index - 2 * step))
            pic_index += 1
            # y_index += 0
            
            if pic_index == len(country_pics):
                pic_index = 0


# end_string = '\n' + '#' * 70 + '\n'
# print(table, end=end_string)
# print(table.query("country == 'Ru'"), end=end_string)
# print(table.query("country == 'Ru' and city == 'Moscow'"), end=end_string)

# table = set_value('Ru', 'Moscow', 'money', 1234567)
# table = change_value('Ru', 'Moscow', 'money', -100)

# print(table.query("country == 'Ru' and city == 'Moscow'"), end=end_string)



class Map:
    def __init__(self):
        self.w = 1
        self.h = 25
        self.width_size = 300
        self.height_size = 1050
        self.cur_cell = None
        self.size_w = self.width_size // self.w
        self.size_h = self.height_size // self.h
    def draw(self, win):
        # вертикальные линии 
        y_index = H // 3
        for line in range(self.w + 1):
            pg.draw.line(win, (0, 0, 0), (line * self.size_w, 0), (line * self.size_w, self.height_size))
        
        # горизонтальная линии 
        for line in range(self.h + 1):
            pg.draw.line(win, (0, 0, 0), (0, line * self.size_h), (self.width_size, line * self.size_h))
    
    def check_highlite_cursor(self, win):
        x, y = pg.mouse.get_pos()
        global index_x, index_y
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
            
        print(index_x, index_y)
            
            
        #rint(table.iloc[index_x, index_y])
#index location
# table =  #
# print(change_value(table, table.iloc[4, 0], table.iloc[0, 1], 'money', 5000))