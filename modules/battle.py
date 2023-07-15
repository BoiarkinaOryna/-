import random
import modules.data_base as m_data
import modules.settings as m_settings
import modules.coordinates as m_coordinates
import modules.ship_destraction as m_destruction
def strike(x_click, y_click, window, start, list_coordinates_x, list_cells, checked_cells):
    if start:
        print("list_cells =", list_cells)
        index_x = -1
        index_y = -1
        for count_x in list_coordinates_x:
            index_x = index_x + 1
            if index_x < 10:
                # print("index_x =", index_x)
                # print("x_click =", x_click)
                # print("list_coordinates_x[index_x] =", list_coordinates_x[index_x])
                # print("list_coordinates_x[index_x + 1] =",list_coordinates_x[index_x + 1])
                    # print("B")
                if x_click >= list_coordinates_x[index_x] and x_click < list_coordinates_x[index_x + 1]:
                    for count_y in m_data.list_coordinates_y:
                        index_y = index_y + 1
                        m_coordinates.search_index(cor_x = count_x, cor_y = count_y)
                        # print("checked_cells =", checked_cells)
                        print("1m_data.index =", m_data.index)
                        for index in checked_cells:
                            print("index in battle =", index)
                            if index != m_data.index:
                                print("A")
                                if index_y < 10:
                                    print("y_click =", y_click)
                                    print("m_data.list_coordinates_y[index_y] =", m_data.list_coordinates_y[index_y])
                                    print("m_data.list_coordinates_y[index_y + 1] =", m_data.list_coordinates_y[index_y + 1])
                                    if y_click >= m_data.list_coordinates_y[index_y] and y_click < m_data.list_coordinates_y[index_y + 1]:
                                        print("2m_data.index =", m_data.index)
                                        checked_cells.append(m_data.index)
                                        print("cheched_cells =", checked_cells)
                                        if list_cells[m_data.index] == 0 or list_cells[m_data.index] == 5 or list_cells[m_data.index] == 10:
                                            cross = m_settings.Cross(x1 = count_x + 5, y1 = count_y + 5)
                                            cross.blit_sprite(screen_game = window)
                                            list_cells[m_data.index] = 10
                                            break
                                        else:
                                            explosion = m_settings.Explosion(x1 = count_x + 5, y1 = count_y + 5)
                                            explosion.blit_sprite(screen_game = window)
                                            # print(list_cells)
                                            m_destruction.defated_ship(list_cells1 = list_cells, index1 = m_data.index, x1 = count_x, y1 = count_y, screen1 = window)
                                            break
                                    break
def control_step(screen, x, y):
    if m_data.bot_step == False:
        strike(x_click = x, y_click = y, window = screen, start = m_data.battle_start, list_coordinates_x = m_data.bot_list_coordinates_x, list_cells = m_data.bot_list_cells, checked_cells = m_data.bot_cells)
        m_data.bot_step = True
    if m_data.bot_step == True:
        click_x = random.randint(106, 460)
        click_y = random.randint(91, 437)
        strike(x_click = click_x, y_click = click_y, window = screen, start = m_data.battle_start, list_coordinates_x = m_data.list_coordinates_x, list_cells = m_data.list_cells, checked_cells = m_data.self_cells)
        m_data.bot_step = False