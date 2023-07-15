import modules.data_base as m_data

def victory(list_cells1):
    count = 0
    for value in list_cells1:
        if value == 11 or value == 12 or value == 13 or value == 14:
            count += 1
            if count == 20:
                m_data.installed_or_not_installed_ships = 2