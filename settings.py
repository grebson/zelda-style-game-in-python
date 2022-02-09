# game setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = './images/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = "#111111"
TEXT_COLOR = '#eeeeee'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'image': './images/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'image': './images/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'image': './images/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'image': './images/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'image': './images/weapons/sai/full.png'}
}