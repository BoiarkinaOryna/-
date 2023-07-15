import pygame
import modules.data_base as m_data
import modules.fixing_ships as m_fixing

pygame.init()

def step(window_game, x_click, y_click, my_ship):
    
        if my_ship == None:
            pass
        elif x_click >= 106 and x_click <= 460:
            if y_click >= 91 and y_click <= 437:
                index_x = -1
                index_y = -1
                for count_x in m_data.list_coordinates_x:
                    index_x = index_x + 1
                    if index_x + 1 < 11:
                        if x_click >= m_data.list_coordinates_x[index_x] and x_click <= m_data.list_coordinates_x[index_x + 1]:
                            for count_y in m_data.list_coordinates_y:
                                index_y = index_y + 1
                                search_index(cor_x = count_x, cor_y = count_y)
                                if index_y + 1 < 11:
                                    if y_click >= m_data.list_coordinates_y[index_y] and y_click <= m_data.list_coordinates_y[index_y + 1]:
                                        my_ship.X = count_x
                                        my_ship.Y = count_y
                                        blit_ship = m_fixing.stop_fixing_ships(ship_index = m_data.num_ship)
                                        # print("blit_ship = " + str(blit_ship))
                                        if blit_ship == True:
                                            changing_list_cells(rotation = m_data.rotate_ship, list_cells = m_data.list_cells, num_ship = m_data.num_ship, index = m_data.index)
                                            # print("bool_drawing after changing_list_cells = " + str(m_data.bool_drawing))
                                            if m_data.bool_drawing == False:
                                                pass
                                            elif m_data.bool_drawing == True:
                                                my_ship.blit_sprite(screen_game = window_game, flip = m_data.rotate_ship)
                                                m_data.bool_drawing = False
                                                m_data.ships_stop_rotation = True
                                                m_data.num_step += 1
                                                # print(m_data.list_cells)
                                                # print(m_data.num_ship)
                                        elif blit_ship == None:
                                            m_data.rotate_ship = False
def tens(n, t_index):
    index = t_index + (n)
    tens = index // 10
    return tens

def changing_list_cells(rotation, list_cells, num_ship, index):
    # print("num_step = " + str(m_data.num_step))
    # print("index = " + str(index))
    # print("rotate_ship in changing_list_cells = " + str(rotation))
    units = index % 10
    # print("units = " + str(units))
    sh_tens = index // 10
    if rotation == True:
        if m_data.num_step == 0:
            if index < 70:
                num_ship = 4
                list_cells[index] = num_ship
                list_cells[index + 10] = num_ship
                list_cells[index + 20] = num_ship
                list_cells[index + 30] = num_ship
                cur_tens = tens(n = - 1, t_index = index)
                if index - 1 >= 0 and sh_tens == cur_tens and list_cells[index - 1] == 0:
                    list_cells[index - 1] = 5
                cur_tens = tens(+ 1, t_index = index)
                if index + 1 <= 99 and sh_tens == cur_tens and list_cells[index + 1] == 0:
                    list_cells[index + 1] = 5
                cur_tens = tens(- 10, t_index = index)
                if index - 10 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 10] == 0:
                    list_cells[index - 10] = 5
                cur_tens = tens(- 11, t_index = index)
                if index - 11 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 11] == 0:
                    list_cells[index - 11] = 5
                cur_tens = tens(- 9, t_index = index)
                if index - 9 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 9] == 0:
                    list_cells[index - 9] = 5
                cur_tens = tens(9, t_index = index)
                if index + 9 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 9] == 0:
                    list_cells[index + 9] = 5
                cur_tens = tens(11, t_index = index)                
                if index + 11 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 11] == 0 :
                    list_cells[index + 11] = 5
                cur_tens = tens(19, t_index = index)
                if index + 19 <= 99 and sh_tens == cur_tens - 2 and list_cells[index + 19] == 0:
                    list_cells[index + 19] = 5
                cur_tens = tens(21, t_index = index)
                if index + 21 <= 99 and sh_tens == cur_tens - 2 and list_cells[index + 21] == 0:
                    list_cells[index + 21] = 5
                cur_tens = tens(29, t_index = index)
                if index + 29 <= 99 and sh_tens == cur_tens - 3 and list_cells[index + 29] == 0:
                    list_cells[index + 29] = 5
                cur_tens = tens(31, t_index = index)
                if index + 31 <= 99 and sh_tens == cur_tens - 3 and list_cells[index + 31] == 0:
                    list_cells[index + 31] = 5
                cur_tens = tens(39, t_index = index)
                if index + 39 <= 99 and sh_tens == cur_tens - 4 and list_cells[index + 39] == 0:
                    list_cells[index + 39] = 5
                cur_tens = tens(40, t_index = index)
                if index + 40 <= 99 and sh_tens == cur_tens - 4 and list_cells[index + 40] == 0:
                    list_cells[index + 40] = 5
                cur_tens = tens(41, t_index = index)
                if index + 41 <= 99 and sh_tens == cur_tens - 4 and list_cells[index + 41] == 0:
                    list_cells[index + 41] = 5
                
                m_data.bool_drawing = True
                # print("bool_drawing in changing_list_cells = " + str(m_data.bool_drawing))
        elif m_data.num_step == 1 or m_data.num_step == 2:
            if index < 80:
                num_ship = 3
                list_cells[index] = num_ship
                list_cells[index + 10] = num_ship
                list_cells[index + 20] = num_ship
                cur_tens = tens(-1, t_index = index)
                if index - 1 >= 0 and sh_tens == cur_tens and list_cells[index - 1] == 0:
                    list_cells[index - 1] = 5
                cur_tens = tens(1, t_index = index)
                if index + 1 <= 99 and sh_tens == cur_tens and list_cells[index + 1] == 0:
                    list_cells[index + 1] = 5
                cur_tens = tens(-10, t_index = index)
                if index - 10 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 10] == 0:
                    list_cells[index - 10] = 5
                cur_tens = tens(-11, t_index = index)
                if index - 11 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 11] == 0:
                    list_cells[index - 11] = 5
                cur_tens = tens(-9, t_index = index)
                if index - 9 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 9] == 0:
                    list_cells[index - 9] = 5
                cur_tens = tens(9, t_index = index)
                if index + 9 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 9] == 0:
                    list_cells[index + 9] = 5
                cur_tens = tens(11, t_index = index)
                if index + 11 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 11] == 0:
                    list_cells[index + 11] = 5
                cur_tens = tens(19, t_index = index)
                if index + 19 <= 99 and sh_tens == cur_tens - 2 and list_cells[index + 19] == 0:
                    list_cells[index + 19] = 5
                cur_tens = tens(21, t_index = index)
                if index + 21 <= 99 and sh_tens == cur_tens - 2 and list_cells[index + 21] == 0:
                    list_cells[index + 21] = 5
                cur_tens = tens(29, t_index = index)
                if index + 29 <= 99 and sh_tens == cur_tens - 3 and list_cells[index + 29] == 0:
                    list_cells[index + 29] = 5
                cur_tens = tens(31, t_index = index)
                if index + 31 <= 99 and sh_tens == cur_tens - 3 and list_cells[index + 31] == 0:
                    list_cells[index + 31] = 5
                cur_tens = tens(30, t_index = index)
                if index + 30 <= 99 and sh_tens == cur_tens - 3 and list_cells[index + 30] == 0:
                    list_cells[index + 30] = 5
                m_data.bool_drawing = True
                # print("bool_drawing in changing_list_cells = " + str(m_data.bool_drawing))
        elif m_data.num_step == 3 or m_data.num_step == 4 or m_data.num_step == 5:
            if index < 90:
                num_ship = 2
                list_cells[index] = num_ship
                cur_tens = tens(9, t_index = index)
                if index - 1 >= 0 and sh_tens == cur_tens and list_cells[index + 9] == 0:
                    list_cells[index + 9] = num_ship
                list_cells[index + 10] = num_ship
                cur_tens = tens(-1, t_index = index)
                if index - 1 >= 0 and sh_tens == cur_tens and list_cells[index - 1] == 0:
                    list_cells[index - 1] = 5
                cur_tens = tens(1, t_index = index)
                if index + 1 <= 99 and sh_tens == cur_tens and list_cells[index + 1] == 0:
                    list_cells[index + 1] = 5
                cur_tens = tens(-10, t_index = index)
                if index - 10 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 10] == 0:
                    list_cells[index - 10] = 5
                cur_tens = tens(-11, t_index = index)
                if index - 11 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 11] == 0:
                    list_cells[index - 11] = 5
                cur_tens = tens(-9, t_index = index)
                if index - 9 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 9] == 0:
                    list_cells[index - 9] = 5
                cur_tens = tens(9, t_index = index)
                if index + 9 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 9] == 0:
                    list_cells[index + 9] = 5
                cur_tens = tens(11, t_index = index)
                if index + 11 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 11] == 0:
                    list_cells[index + 11] = 5
                cur_tens = tens(19, t_index = index)
                if index + 19 <= 99 and sh_tens == cur_tens - 2 and list_cells[index + 19] == 0:
                    list_cells[index + 19] = 5
                cur_tens = tens(20, t_index = index)
                if index + 20 <= 99 and sh_tens == cur_tens - 2 and list_cells[index + 20] == 0:
                    list_cells[index + 20] = 5
                cur_tens = tens(21, t_index = index)
                if index + 21 <= 99 and sh_tens == cur_tens - 2 and list_cells[index + 21] == 0:
                    list_cells[index + 21] = 5
                m_data.bool_drawing = True
                # print("bool_drawing in changing_list_cells = " + str(m_data.bool_drawing))
        elif m_data.num_step == 6 or m_data.num_step == 7 or m_data.num_step == 8 or m_data.num_step == 9:
            num_ship = 1
            cur_tens = tens(-1, t_index = index)
            if index - 1 >= 0 and sh_tens == cur_tens and list_cells[index - 1] == 0:
                list_cells[index - 1] = 5
            cur_tens = tens(1, t_index = index)
            if index + 1 <= 99 and sh_tens == cur_tens and list_cells[index + 1] == 0:
                list_cells[index + 1] = 5
            cur_tens = tens(-10, t_index = index)
            if index - 10 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 10] == 0:
                list_cells[index - 10] = 5
            cur_tens = tens(-11, t_index = index)
            if index - 11 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 11] == 0:
                list_cells[index - 11] = 5
            cur_tens = tens(-9, t_index = index)
            if index - 9 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 9] == 0:
                list_cells[index - 9] = 5
            cur_tens = tens(9, t_index = index)
            if index + 9 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 9] == 0:
                list_cells[index + 9] = 5
            cur_tens = tens(10, t_index = index)
            if index + 10 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 10] == 0:
                list_cells[index + 10] = 5
            cur_tens = tens(11, t_index = index)
            if index + 11 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 11] == 0:
                list_cells[index + 11] = 5
            list_cells[index] = num_ship
            m_data.bool_drawing = True
            # print("bool_drawing in changing_list_cells = " + str(m_data.bool_drawing))
    elif rotation == False:
        if  m_data.num_step == 0:
            if units != 7 and units != 8 and units != 9:
                num_ship = 4
                list_cells[index] = num_ship
                list_cells[index + 1] = num_ship
                list_cells[index + 2] = num_ship
                list_cells[index + 3] = num_ship
                cur_tens = tens(4, t_index = index)
                if index - 1 >= 0 and sh_tens == cur_tens:
                    list_cells[index + 4] = 5
                cur_tens = tens(-1, t_index = index)
                if index - 1 >= 0 and sh_tens == cur_tens and list_cells[index - 1] == 0:
                    list_cells[index - 1] = 5
                cur_tens = tens(-11, t_index = index)
                if index - 11 >= 0 and sh_tens == cur_tens + 1:
                    list_cells[index - 11] = 5
                cur_tens = tens(-10, t_index = index)
                if index - 10 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 10] == 0:
                    list_cells[index - 10] = 5
                cur_tens = tens(-9, t_index = index)
                if index - 9 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 9] == 0:
                    list_cells[index - 9] = 5
                cur_tens = tens(-8, t_index = index)
                if index - 8 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 8] == 0:
                    list_cells[index - 8] = 5
                cur_tens = tens(-7, t_index = index)
                if index - 7 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 7] == 0:
                    list_cells[index - 7] = 5
                cur_tens = tens(-6, t_index = index)
                if index - 6 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 6] == 0:
                    list_cells[index - 6] = 5
                cur_tens = tens(9, t_index = index)
                if index + 9 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 9] == 0:
                    list_cells[index + 9] = 5
                cur_tens = tens(10, t_index = index)
                if index + 10 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 10] == 0:      
                    list_cells[index + 10] = 5
                cur_tens = tens(11, t_index = index)
                if index + 11 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 11] == 0:
                    list_cells[index + 11] = 5
                cur_tens = tens(12, t_index = index)
                if index + 12 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 12] == 0:
                    list_cells[index + 12] = 5
                cur_tens = tens(13, t_index = index)
                if index + 13 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 13] == 0:
                    list_cells[index + 13] = 5
                cur_tens = tens(14, t_index = index)
                if index + 14 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 14] == 0:
                    list_cells[index + 14] = 5
                
                m_data.bool_drawing = True
                # print("bool_drawing in changing_list_cells = " + str(m_data.bool_drawing))
        elif m_data.num_step == 1 or m_data.num_step == 2:
            # print("units = " + str(units))
            if units != 8 and units != 9:
                num_ship = 3
                list_cells[index] = num_ship
                list_cells[index + 1] = num_ship
                list_cells[index + 2] = num_ship
                cur_tens = tens(3, t_index = index)
                if index + 3 <= 99 and sh_tens == cur_tens:
                    list_cells[index + 3] = 5
                cur_tens = tens(-1, t_index = index)
                if index - 1 >= 0 and sh_tens == cur_tens and list_cells[index - 1] == 0:
                    list_cells[index - 1] = 5
                cur_tens = tens(-11, t_index = index)
                if index - 11 >= 0 and sh_tens == cur_tens + 1:
                    list_cells[index - 11] = 5
                cur_tens = tens(-10, t_index = index)
                if index - 10 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 10] == 0:
                    list_cells[index - 10] = 5
                cur_tens = tens(-9, t_index = index)
                if index - 9 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 9] == 0:
                    list_cells[index - 9] = 5
                cur_tens = tens(-8, t_index = index)
                if index - 8 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 8] == 0:
                    list_cells[index - 8] = 5
                cur_tens = tens(-7, t_index = index)
                if index - 7 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 7] == 0:
                    list_cells[index - 7] = 5
                cur_tens = tens(9, t_index = index)
                if index + 9 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 9] == 0:
                    list_cells[index + 9] = 5
                cur_tens = tens(10, t_index = index)
                if index + 10 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 10] == 0:
                    list_cells[index + 10] = 5
                cur_tens = tens(11, t_index = index)
                if index + 11 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 11] == 0:
                    list_cells[index + 11] = 5
                cur_tens = tens(12, t_index = index)
                if index + 12 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 12] == 0:
                    list_cells[index + 12] = 5
                cur_tens = tens(13, t_index = index)
                if index + 13 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 13] == 0:
                    list_cells[index + 13] = 5
                
                m_data.bool_drawing = True
                # print("bool_drawing in changing_list_cells = " + str(m_data.bool_drawing))
        elif m_data.num_step == 3 or m_data.num_step == 4 or m_data.num_step == 5:
            if not units == 9:
                num_ship = 2
                list_cells[index] = num_ship
                list_cells[index + 1] = num_ship
                cur_tens = tens(2, t_index = index)
                if index + 2 <= 99 and sh_tens == cur_tens:
                    list_cells[index + 2] = 5
                cur_tens = tens(-1, t_index = index)
                if index - 1 >= 0 and sh_tens == cur_tens and list_cells[index - 1] == 0:
                    list_cells[index - 1] = 5
                cur_tens = tens(-11, t_index = index)
                if index - 11 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 11] == 0:
                    list_cells[index - 11] = 5
                cur_tens = tens(-10, t_index = index)
                if index - 10 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 10] == 0:
                    list_cells[index - 10] = 5
                cur_tens = tens(- 9, t_index = index)
                if index - 9 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 9] == 0:
                    list_cells[index - 9] = 5
                cur_tens = tens(-8, t_index = index)
                if index - 8 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 8] == 0:
                    list_cells[index - 8] = 5
                cur_tens = tens(9, t_index = index)
                if index + 9 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 9] == 0:
                    list_cells[index + 9] = 5
                cur_tens = tens(10, t_index = index)
                if index + 10 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 10] == 0:
                    list_cells[index + 10] = 5
                cur_tens = tens(11, t_index = index)
                if index + 11 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 11] == 0:
                    list_cells[index + 11] = 5
                cur_tens = tens(12, t_index = index)
                if index + 12 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 12] == 0:
                    list_cells[index + 12] = 5
                m_data.bool_drawing = True
                # print("bool_drawing in changing_list_cells = " + str(m_data.bool_drawing))
        elif m_data.num_step == 6 or m_data.num_step == 7 or m_data.num_step == 8 or m_data.num_step == 9:
            num_ship = 1
            list_cells[index] = num_ship
            cur_tens = tens(1, t_index = index)
            if index + 1 <= 99 and sh_tens == cur_tens:
                list_cells[index + 1] = 5
            cur_tens = tens(-1, t_index = index)
            if index - 1 >= 0 and sh_tens == cur_tens and list_cells[index - 1] == 0:
                    list_cells[index - 1] = 5
            cur_tens = tens(-11, t_index = index)
            if index - 11 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 11] == 0:
                list_cells[index - 11] = 5
            cur_tens = tens(-10, t_index = index)
            if index - 10 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 10] == 0:
                    list_cells[index - 10] = 5
            cur_tens = tens(-9, t_index = index)
            if index - 9 >= 0 and sh_tens == cur_tens + 1 and list_cells[index - 9] == 0:
                list_cells[index - 9] = 5
            cur_tens = tens(9, t_index = index)
            if index + 9 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 9] == 0:
                list_cells[index + 9] = 5
            cur_tens = tens(10, t_index = index)
            if index + 10 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 10] == 0:
                list_cells[index + 10] = 5
            cur_tens = tens(11, t_index = index)
            if index + 11 <= 99 and sh_tens == cur_tens - 1 and list_cells[index + 11] == 0:
                list_cells[index + 11] = 5
            m_data.bool_drawing = True
            # print("bool_drawing in changing_list_cells = " + str(m_data.bool_drawing))
def search_index(cor_x, cor_y):
    # print("m_data.bot_list_coordinates_x[8] =", m_data.bot_list_coordinates_x[8])
    # print("searching_index")
    # print("cor x =", cor_x)
    # print("cor y =", cor_y)
    if cor_x == 106 or cor_x == m_data.bot_list_coordinates_x[0]:
        if cor_y == 91:
            m_data.index = 0
        elif cor_y == 126:
            m_data.index = 1
        elif cor_y == 160:
            m_data.index = 2
        elif cor_y == 195:
            m_data.index = 3   
        elif cor_y == 230:
            m_data.index = 4 
        elif cor_y == 264:
            m_data.index = 5 
        elif cor_y == 300:
            m_data.index = 6
        elif cor_y == 333:
            m_data.index = 7 
        elif cor_y == 369:
            m_data.index = 8
        elif cor_y == 402:
            m_data.index = 9
    elif cor_x == 141 or cor_x == m_data.bot_list_coordinates_x[1]:
        if cor_y == 91:
            m_data.index = 10
        elif cor_y == 126:
            m_data.index = 11
        elif cor_y == 160:
            m_data.index = 12
        elif cor_y == 195:
            m_data.index = 13  
        elif cor_y == 230:
            m_data.index = 14
        elif cor_y == 264:
            m_data.index = 15
        elif cor_y == 300:
            m_data.index = 16 
        elif cor_y == 333:
            m_data.index = 17 
        elif cor_y == 369:
            m_data.index = 18 
        elif cor_y == 402:
            m_data.index = 19
    elif cor_x == 177 or cor_x == m_data.bot_list_coordinates_x[2]:
        if cor_y == 91:
            m_data.index = 20
        elif cor_y == 126:
            m_data.index = 21
        elif cor_y == 160:
            m_data.index = 22
        elif cor_y == 195:
            m_data.index = 23
        elif cor_y == 230:
            m_data.index = 24
        elif cor_y == 264:
            m_data.index = 25 
        elif cor_y == 300:
            m_data.index = 26 
        elif cor_y == 333:
            m_data.index = 27 
        elif cor_y == 369:
            m_data.index = 28 
        elif cor_y == 402:
            m_data.index = 29 
    elif cor_x == 212 or cor_x == m_data.bot_list_coordinates_x[3]:
        if cor_y == 91:
            m_data.index = 30
        elif cor_y == 126:
            m_data.index = 31
        elif cor_y == 160:
            m_data.index = 32
        elif cor_y == 195:
            m_data.index = 33   
        elif cor_y == 230:
            m_data.index = 34
        elif cor_y == 264:
            m_data.index = 35
        elif cor_y == 300:
            m_data.index = 36 
        elif cor_y == 333:
            m_data.index = 37 
        elif cor_y == 369:
            m_data.index = 38 
        elif cor_y == 402:
            m_data.index = 39 
    elif cor_x == 248 or cor_x == m_data.bot_list_coordinates_x[4]:
        if cor_y == 91:
            m_data.index = 40
        elif cor_y == 126:
            m_data.index = 41
        elif cor_y == 160:
            m_data.index = 42
        elif cor_y == 195:
            m_data.index = 43   
        elif cor_y == 230:
            m_data.index = 44
        elif cor_y == 264:
            m_data.index = 45 
        elif cor_y == 300:
            m_data.index = 46
        elif cor_y == 333:
            m_data.index = 47
        elif cor_y == 369:
            m_data.index = 48 
        elif cor_y == 402:
            m_data.index = 49
    elif cor_x == 283 or cor_x == m_data.bot_list_coordinates_x[5]:
        if cor_y == 91:
            m_data.index = 50
        elif cor_y == 126:
            m_data.index = 51
        elif cor_y == 160:
            m_data.index = 52
        elif cor_y == 195:
            m_data.index = 53   
        elif cor_y == 230:
            m_data.index = 54 
        elif cor_y == 264:
            m_data.index = 55
        elif cor_y == 300:
            m_data.index = 56 
        elif cor_y == 333:
            m_data.index = 57 
        elif cor_y == 369:
            m_data.index = 58
        elif cor_y == 402:
            m_data.index = 59
    elif cor_x == 319 or cor_x == m_data.bot_list_coordinates_x[6]:
        if cor_y == 91:
            m_data.index = 60
        elif cor_y == 126:
            m_data.index = 61
        elif cor_y == 160:
            m_data.index = 62
        elif cor_y == 195:
            m_data.index = 63   
        elif cor_y == 230:
            m_data.index = 64
        elif cor_y == 264:
            m_data.index = 65
        elif cor_y == 300:
            m_data.index = 66 
        elif cor_y == 333:
            m_data.index = 67 
        elif cor_y == 369:
            m_data.index = 68 
        elif cor_y == 402:
            m_data.index = 69 
    elif cor_x == 354 or cor_x == m_data.bot_list_coordinates_x[7]:
        if cor_y == 91:
            m_data.index = 70
        elif cor_y == 126:
            m_data.index = 71
        elif cor_y == 160:
            m_data.index = 72
        elif cor_y == 195:
            m_data.index = 73 
        elif cor_y == 230:
            m_data.index = 74 
        elif cor_y == 264:
            m_data.index = 75 
        elif cor_y == 300:
            m_data.index = 76 
        elif cor_y == 333:
            m_data.index = 77 
        elif cor_y == 369:
            m_data.index = 78 
        elif cor_y == 402:
            m_data.index = 79
    elif cor_x == 390 or cor_x == m_data.bot_list_coordinates_x[8]:
        if cor_y == 91:
            m_data.index = 80
        elif cor_y == 126:
            m_data.index = 81
        elif cor_y == 160:
            m_data.index = 82
        elif cor_y == 195:
            m_data.index = 83  
        elif cor_y == 230:
            m_data.index = 84 
        elif cor_y == 264:
            m_data.index = 85
        elif cor_y == 300:
            m_data.index = 86
        elif cor_y == 333:
            m_data.index = 87 
        elif cor_y == 369:
            m_data.index = 88
        elif cor_y == 402:
            m_data.index = 89
    elif cor_x == 425 or cor_x == m_data.bot_list_coordinates_x[9]:
        if cor_y == 91:
            m_data.index = 90
        elif cor_y == 126:
            m_data.index = 91
        elif cor_y == 160:
            m_data.index = 92
        elif cor_y == 195:
            m_data.index = 93
        elif cor_y == 230:
            m_data.index = 94
        elif cor_y == 264:
            m_data.index = 95
        elif cor_y == 300:
            m_data.index = 96
        elif cor_y == 333:
            m_data.index = 97
        elif cor_y == 369:
            m_data.index = 98
        elif cor_y == 402:
            m_data.index = 99