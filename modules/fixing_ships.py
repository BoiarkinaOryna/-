import modules.data_base as m_data

def stop_fixing_ships(ship_index):
    ship_cells1 = find_ship_cells(coordinate = m_data.index)
    # print("ship_cells1 = " + str(ship_cells1))
    # print("in the function stop_fixing_ships")
    if ship_cells1 != []:
        for index in ship_cells1:
            # print("Hello1")
            if m_data.list_cells[index] != 0:
                # print("rotate_ship in stop_fixing_ships = " + str(m_data.rotate_ship))
                # print("Hello2")
                return False
        # for index in ship_cells1:
            else:
                m_data.list_cells[index] = ship_index
            # print("")
        return True

def find_ship_cells(coordinate):
    ship_cells = []
    if m_data.num_step == 0:
        length = 4
    elif m_data.num_step == 1 or m_data.num_step == 2:
        length = 3
    elif m_data.num_step == 3 or m_data.num_step == 4 or m_data.num_step == 5:
        length = 2
    elif m_data.num_step == 6 or m_data.num_step == 7 or m_data.num_step == 8 or m_data.num_step == 9:
        length = 1
    if m_data.rotate_ship == False:
        for count in range(length):
            index = coordinate + count
            # print("index = " + str(index))
            if index <= 99:
                ship_cells.append(index)
            else:
                # print("return1")
                return []
    elif m_data.rotate_ship == True:
        for count in range(length):
            index = coordinate + count * 10
            if index <= 99:
                ship_cells.append(index)
            else:
                # print("return2")
                return []
    
    for cell_index in ship_cells:
        # print("cell_index = " + str(cell_index))
        if m_data.list_cells[cell_index] != 0:
            # print("list_cells = " + str(m_data.list_cells))
            # print("list_cells[cell_index] = " + str(m_data.list_cells[cell_index]))
            # print("return3")
            return []
    # print("return4")
    return ship_cells
