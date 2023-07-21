import random
import modules.settings as m_settings
import modules.victory as m_victory

def broken_ship(list_cells, index, x, y, screen):
    value = list_cells[index]
    if value == 14:
        if index + 10 <= 99 and index + 20 <= 99 and index + 30 <= 99:
            if list_cells[index + 10] == value and list_cells[index + 20] == value and list_cells[index + 30] == value:
                ship4 = m_settings.Ship4(x1 = x, y1 = y, name_file1 = "images/broken4.png")
                ship4.blit_sprite(screen_game = screen, flip = True)
        if index + 10 <= 99 and index + 20 <= 99 and index - 10 <= 99:
            if list_cells[index + 10] == value and list_cells[index + 20] == value and list_cells[index - 10] == value:
                ship4 = m_settings.Ship4(x1 = x - 35, y1 = y, name_file1 = "images/broken4.png")
                ship4.blit_sprite(screen_game = screen, flip = True)
        if index + 10 <= 99 and index - 20 <= 99 and index - 10 <= 99:
            if list_cells[index + 10] == value and list_cells[index - 20] == value and list_cells[index - 10] == value:
                ship4 = m_settings.Ship4(x1 = x - 70, y1 = y, name_file1 = "images/broken4.png")
                ship4.blit_sprite(screen_game = screen, flip = True)
        if index - 10 <= 99 and index - 20 <= 99 and index - 30 <= 99:
            if list_cells[index - 10] == value and list_cells[index - 20] == value and list_cells[index - 30] == value:
                ship4 = m_settings.Ship4(x1 = x - 105, y1 = y, name_file1 = "images/broken4.png")
                ship4.blit_sprite(screen_game = screen, flip = True)
        if index + 1 <= 99 and index + 2 <= 99 and index + 3 <= 99:
            if list_cells[index + 1] == value and list_cells[index + 2] == value and list_cells[index + 3] == value:
                ship4 = m_settings.Ship4(x1 = x, y1 = y, name_file1 = "images/broken4.png")
                ship4.blit_sprite(screen_game = screen, flip = False)
        if index + 1 <= 99 and index + 2 <= 99 and index - 1 <= 99:
            if list_cells[index + 1] == value and list_cells[index + 2] == value and list_cells[index - 1] == value:
                ship4 = m_settings.Ship4(x1 = x, y1 = y - 35, name_file1 = "images/broken4.png")
                ship4.blit_sprite(screen_game = screen, flip = False)
        if index + 1 <= 99 and index - 2 <= 99 and index - 1 <= 99:
            if list_cells[index + 1] == value and list_cells[index - 2] == value and list_cells[index - 1] == value:
                ship4 = m_settings.Ship4(x1 = x, y1 = y - 70, name_file1 = "images/broken4.png")
                ship4.blit_sprite(screen_game = screen, flip = False)
        if index - 1 <= 99 and index - 2 <= 99 and index - 3 <= 99:
            if list_cells[index - 1] == value and list_cells[index - 2] == value and list_cells[index - 3] == value:
                ship4 = m_settings.Ship4(x1 = x, y1 = y - 105, name_file1 = "images/broken4.png")
                ship4.blit_sprite(screen_game = screen, flip = False)
    if value == 13:
        if index + 1 <= 99 and index + 2 <= 99:
            if index // 10 == (index + 1) // 10 and (index + 1) // 10 == (index + 2) // 10:
                if list_cells[index + 1] == value and list_cells[index + 2] == value:
                    ship3 = m_settings.Ship3(x1 = x, y1 = y, name_file1 = "images/broken3.png")
                    ship3.blit_sprite(screen_game = screen, flip = False)
        if index - 1 <= 99 and index + 1 <= 99:
            if index // 10 == (index - 1) // 10 and (index - 1) // 10 == (index + 1) // 10:
                if list_cells[index - 1] == value and list_cells[index + 1] == value:
                    ship3 = m_settings.Ship3(x1 = x, y1 = y - 35, name_file1 = "images/broken3.png")
                    ship3.blit_sprite(screen_game = screen, flip = False)
        if index - 2 <= 99 and index - 1 <= 99:
            if index // 10 == (index - 1) // 10 and (index - 1) // 10 == (index - 2) // 10:
                if list_cells[index - 2] == value and list_cells[index - 1] == value:
                    ship3 = m_settings.Ship3(x1 = x, y1 = y - 70, name_file1 = "images/broken3.png")
                    ship3.blit_sprite(screen_game = screen, flip = False)
        if index + 10 <= 99 and index + 20 <= 99:
            if list_cells[index + 10] == value and list_cells[index + 20] == value:
                ship3 = m_settings.Ship3(x1 = x, y1 = y, name_file1 = "images/broken3.png")
                ship3.blit_sprite(screen_game = screen, flip = True)
        if index - 10 <= 99 and index + 10 <= 99:
            if list_cells[index - 10] == value and list_cells[index + 10] == value:
                ship3 = m_settings.Ship3(x1 = x - 35, y1 = y, name_file1 = "images/broken3.png")
                ship3.blit_sprite(screen_game = screen, flip = True)
        if index - 20 <= 99 and index - 10 <= 99:
            if list_cells[index - 20] == value and list_cells[index - 10] == value:
                ship3 = m_settings.Ship3(x1 = x - 70, y1 = y, name_file1 = "images/broken3.png")
                ship3.blit_sprite(screen_game = screen, flip = True)
    if value == 12:
        if index + 1 <= 99:
            if index // 10 == (index + 1) // 10:
                if list_cells[index + 1] == value:
                    ship2 = m_settings.Ship2(x1 = x, y1 = y, name_file1 = "images/broken2.png")
                    ship2.blit_sprite(screen_game = screen, flip = False)
        if index - 1 <= 99:
            if index // 10 == (index - 1) // 10:
                if list_cells[index - 1] == value:
                    ship2 = m_settings.Ship2(x1 = x, y1 = y - 35, name_file1 = "images/broken2.png")
                    ship2.blit_sprite(screen_game = screen, flip = False)
        if index + 10 <= 99:
            if list_cells[index + 10] == value:
                ship2 = m_settings.Ship2(x1 = x, y1 = y, name_file1 = "images/broken2.png")
                ship2.blit_sprite(screen_game = screen, flip = True)
        if index - 10 <= 99:
            if list_cells[index - 10] == value:
                ship2 = m_settings.Ship2(x1 = x - 35, y1 = y, name_file1 = "images/broken2.png")
                ship2.blit_sprite(screen_game = screen, flip = True)
    if value == 11:
            print("1")
            ship1 = m_settings.Ship1(x1 = x, y1 = y, name_file1 = "images/broken1.png")
            bool = random.choice([True, False])
            ship1.blit_sprite(screen_game = screen, flip = bool)

    m_victory.victory(list_cells1 = list_cells)
def defated_ship(list_cells1, index1, x1, y1, screen1):
    if list_cells1[index1] == 4:
        list_cells1[index1] = 14
    elif list_cells1[index1] == 3:
        list_cells1[index1] = 13
    elif list_cells1[index1] == 2:
        list_cells1[index1] = 12
    elif list_cells1[index1] == 1:
        list_cells1[index1] = 11
    print("list_cells1 =", list_cells1)
    broken_ship(list_cells = list_cells1, index = index1, x = x1, y = y1, screen = screen1)