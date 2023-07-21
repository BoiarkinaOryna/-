import pygame
import modules.settings as m_settings
import modules.data_base as m_data
import modules.coordinates as m_coordinates
import modules.bot_ship_installation as m_installation
pygame.init()

def draw_ship(window, x, y):
    ship4 = m_settings.Ship4(x1 = 100, y1 = 500)
    ship3 = m_settings.Ship3(x1 = 100, y1 = 500)
    ship2 = m_settings.Ship2(x1 = 100, y1 = 500)
    ship1 = m_settings.Ship1(x1 = 100, y1 = 500)
    plain = m_settings.Plain()
    plain.blit_sprite(screen_game= window, flip = False)
    if m_data.installed_or_not_installed_ships == False:
        if m_data.ships_stop_rotation == True:
            m_data.my_ship = None
            m_data.rotate_ship = False
            m_data.ships_stop_rotation = False
        if m_data.ships_stop_rotation == False:
            if x >= 0 and x < 250 and y >= 450 and y < 700:
                if m_data.num_step == 0:
                    window.fill((102, 178, 255))
                    m_settings.board.blit_sprite(screen_game = window, flip = False)
                    m_settings.bot_board.blit_sprite(screen_game= window, flip = False)
                    mark = m_settings.Mark()
                    mark.blit_sprite(screen_game= window, flip = False)
                    ship4.blit_sprite(screen_game= window, flip = False)
                    
                    m_data.my_ship = ship4
                    m_data.installed_ship = True
                    # m_data.ship_len = 4
                elif m_data.num_step == 1 or m_data.num_step == 2:
                    ship3.blit_sprite(screen_game= window, flip = False)
                    # m_data.num_step += 1
                    m_data.my_ship = ship3
                    m_data.installed_ship = True
                    # m_data.ship_len = 3
                elif m_data.num_step == 3 or m_data.num_step == 4 or m_data.num_step == 5:
                    ship2.blit_sprite(screen_game= window, flip = False)
                    # m_data.num_step += 1
                    m_data.my_ship = ship2
                    m_data.installed_ship = True
                    # m_data.ship_len = 2
                elif m_data.num_step == 6 or m_data.num_step == 7 or m_data.num_step == 8 or m_data.num_step == 9:
                    ship1.blit_sprite(screen_game= window, flip = False)
                    m_data.my_ship = ship1
                    m_data.installed_ship = True
            elif x > 250 and x < 300 and y > 600 and y < 650:
                flip(window = window, my_ship = m_data.my_ship)
            elif x >= 106 and x <= 460 and y >= 91 and y <= 437:
                m_coordinates.step(window_game = window, x_click = int(x), y_click = int(y), my_ship = m_data.my_ship)
                m_data.installed_ship = False
                if m_data.num_step >= 10:
                    m_data.installed_or_not_installed_ships = True
            
    if m_data.installed_or_not_installed_ships == True:
        m_installation.bot_ship_installation()

def flip(window, my_ship):
    print("my_ship = " + str(my_ship))
    if my_ship == None:
        pass
    
    elif m_data.rotate_ship == False:
        my_ship.X = 100
        my_ship.Y = 500
        m_data.rotate_ship = True
        my_ship.blit_sprite(screen_game= window, flip = True)
    elif m_data.rotate_ship == True:
        my_ship.X = 100
        my_ship.Y = 500
        m_data.rotate_ship = False
        my_ship.blit_sprite(screen_game= window, flip = False)