import random
import modules.data_base as m_data
import modules.coordinates as m_coordinates


def bot_ship_installation():
    ship = 4
    if not m_data.ships_stop_rotation:
        while m_data.bot_num_ship < 10:
            print("m_data.bot_num_ship =", m_data.bot_num_ship)
            print("ship = " + str(ship))
            coordinate = random.randint(0, 99)
            bot_ship_rotation = random.choice([True, False])
            print("1")
            print("bot_ship_rotation =", bot_ship_rotation)
            if bot_ship_rotation == False:
                    print("F2")
                    if coordinate <= 99:
                        print("F3")
                        if m_data.bot_list_cells[coordinate] == 0:
                            units = coordinate % 10
                            print("m_data.bot_num_ship =", m_data.bot_num_ship)
                            print("units =", units)
                            if m_data.bot_num_ship == 0:
                                if units < 7:
                                    if m_data.bot_list_cells[coordinate + 1] == 0 and m_data.bot_list_cells[coordinate + 2] == 0 and m_data.bot_list_cells[coordinate + 3] == 0:
                                        for a in range(4):
                                            m_data.bot_list_cells[coordinate + a] = 4
                                            m_data.num_step = 0
                                            m_coordinates.changing_list_cells(rotation = bot_ship_rotation, list_cells = m_data.bot_list_cells, num_ship = ship, index = coordinate)
                                        m_data.bot_num_ship += 1
                                        
                            if m_data.bot_num_ship == 1 or m_data.bot_num_ship == 2:
                                if units < 8:
                                    if m_data.bot_list_cells[coordinate + 1] == 0 and m_data.bot_list_cells[coordinate + 2] == 0:
                                        for a in range(3):
                                            m_data.bot_list_cells[coordinate + a] = 3
                                            m_data.num_step = 1
                                            m_coordinates.changing_list_cells(rotation = bot_ship_rotation, list_cells = m_data.bot_list_cells, num_ship = ship, index = coordinate)
                                        m_data.bot_num_ship += 1
                                        
                            if m_data.bot_num_ship == 3 or m_data.bot_num_ship == 4 or m_data.bot_num_ship == 5:
                                if units < 9:
                                    if m_data.bot_list_cells[coordinate + 1] == 0:
                                        for a in range(2):
                                            m_data.bot_list_cells[coordinate + a] = 2
                                            m_data.num_step = 3
                                            m_coordinates.changing_list_cells(rotation = bot_ship_rotation, list_cells = m_data.bot_list_cells, num_ship = ship, index = coordinate)
                                        m_data.bot_num_ship += 1
                                            
                            if m_data.bot_num_ship == 6 or m_data.bot_num_ship == 7 or m_data.bot_num_ship == 8 or m_data.bot_num_ship == 9:
                                if m_data.bot_list_cells[coordinate] == 0:
                                    m_data.bot_list_cells[coordinate] = 1
                                    m_data.num_step = 6
                                    m_coordinates.changing_list_cells(rotation = bot_ship_rotation, list_cells = m_data.bot_list_cells, num_ship = ship, index = coordinate)
                                    m_data.bot_num_ship += 1
                                   
            elif bot_ship_rotation == True:
                    print("T2")
                    if coordinate <= 99:
                        print("T3")
                        if m_data.bot_list_cells[coordinate] == 0:
                            tens = coordinate // 10
                            print("m_data.bot_num_ship =", m_data.bot_num_ship)
                            print("tens =", tens)
                            if m_data.bot_num_ship == 0:
                                if tens < 7:
                                    if m_data.bot_list_cells[coordinate + 10] == 0 and m_data.bot_list_cells[coordinate + 20] == 0  and m_data.bot_list_cells[coordinate + 30] == 0:
                                        for a in range(4):
                                            m_data.bot_list_cells[coordinate + a * 10] = 4
                                            m_data.num_step = 0
                                            m_coordinates.changing_list_cells(rotation = bot_ship_rotation, list_cells = m_data.bot_list_cells, num_ship = ship, index = coordinate)
                                        m_data.bot_num_ship += 1
                                            
                            if m_data.bot_num_ship == 1 or m_data.bot_num_ship == 2:
                                if tens < 8:
                                    if m_data.bot_list_cells[coordinate + 10] == 0 and m_data.bot_list_cells[coordinate + 20] == 0:
                                        for a in range(3):
                                            m_data.bot_list_cells[coordinate + a * 10] = 3
                                            m_data.num_step = 1
                                            m_coordinates.changing_list_cells(rotation = bot_ship_rotation, list_cells = m_data.bot_list_cells, num_ship = ship, index = coordinate)
                                        m_data.bot_num_ship += 1
                                            
                            if m_data.bot_num_ship == 3 or m_data.bot_num_ship == 4 or m_data.bot_num_ship == 5:
                                if tens < 9:
                                    if m_data.bot_list_cells[coordinate + 10] == 0:
                                        for a in range(2):
                                            m_data.bot_list_cells[coordinate + a * 10] = 2
                                            m_data.num_step = 3
                                            m_coordinates.changing_list_cells(rotation = bot_ship_rotation, list_cells = m_data.bot_list_cells, num_ship = ship, index = coordinate)
                                        m_data.bot_num_ship += 1
                                            
                            if m_data.bot_num_ship == 6 or m_data.bot_num_ship == 7 or m_data.bot_num_ship == 8 or m_data.bot_num_ship == 9:
                                if m_data.bot_list_cells[coordinate] == 0:
                                    m_data.bot_list_cells[coordinate] = 1
                                    m_data.num_step = 6
                                    m_coordinates.changing_list_cells(rotation = bot_ship_rotation, list_cells = m_data.bot_list_cells, num_ship = ship, index = coordinate)
                                    m_data.bot_num_ship += 1
                                    
    m_data.battle_start = True
    m_data.ships_stop_rotation = True
    # print("bot_list_cells = " + str(m_data.bot_list_cells))
                            