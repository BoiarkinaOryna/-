import modules.settings as m_settings

list_cells = [
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
bot_list_cells = [
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
num_step = 0
count_ship = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
my_ship = m_settings.Ship4(x1 = 100, y1 = 500)
rotate_ship = False
list_coordinates_x = (
    106, 141, 177, 212, 248, 283, 319, 354, 390, 425, 460
)
list_coordinates_y = (
    91, 126, 160, 195, 230, 264, 300, 333, 369, 402, 437
)
bot_list_coordinates_x = (
    566, 601, 637, 672, 708, 743, 779, 814, 850, 885, 920
)
ships_stop_rotation = False

installed_or_not_installed_ships = False
installed_ship = False
num_ship = 5
index = 0
bool_drawing = False
stop_bot_ship_rotaion = False
battle_start = False
bot_step = False
self_cells = [-1]
bot_cells = [-1]
bot_num_ship = 0