import pygame
import modules.settings as m_settings
import modules.choose_ship as m_ship
import modules.battle as m_battle
import modules.data_base as m_data

pygame.init()
FPS = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 700))

screen.fill((102, 178, 255))
m_settings.board.blit_sprite(screen_game = screen, flip = False)
m_settings.bot_board.blit_sprite(screen_game= screen, flip = False)
mark = m_settings.Mark()
mark.blit_sprite(screen_game= screen, flip = False)
game = True

while game:
    
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            lst_x = list(event.pos)
            lst_y = list(event.pos)
            del lst_x[-1]
            del lst_y[-2]
            print(lst_x)
            print(lst_y)
            if m_data.battle_start == False:
                m_ship.draw_ship(window = screen, x = int(lst_x[0]), y = int(lst_y[0]))
            if m_data.battle_start == True:
                m_battle.control_step(screen = screen, x = int(lst_x[0]), y = int(lst_y[0]))
            

    pygame.display.flip()