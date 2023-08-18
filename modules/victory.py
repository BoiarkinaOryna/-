import modules.data_base as m_data
import modules.settings as m_settings

def victory(list_cells1, window):
    count = 0
    for value in list_cells1:
        if value == 11 or value == 12 or value == 13 or value == 14:
            count += 1
            if count == 20:
                print("victory")
                m_data.battle_start = "None"
                reset_button = m_settings.Mark(x1 = 400, y1 = 450, width1 = 200, height1 = 100, name_file1 = "images/reset.png")
                reset_button.blit_sprite(screen_game = window)

def reset(screen1, x, y):
    if x >= 450 and x <= 550 and y >= 500 and y <= 550:
        screen1.fill((102, 178, 255))
        m_settings.board.blit_sprite(screen_game = screen1, flip = False)
        m_settings.bot_board.blit_sprite(screen_game= screen1, flip = False)
        m_settings.mark.blit_sprite(screen_game= screen1, flip = False)
        m_data.battle_start = False
        m_data.list_cells = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
        m_data.bot_list_cells = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
        m_data.num_step = 0
        m_data.ships_stop_rotation = False
        m_data.installed_or_not_installed_ships = False
        m_data.installed_ship = False
        m_data.num_ship = 5
        m_data.index = 0
        m_data.bool_drawing = False
        m_data.stop_bot_ship_rotaion = False
        m_data.battle_start = False
        m_data.bot_step = False
        m_data.bot_num_ship = 0