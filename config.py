# Config.py
config.load_autoconfig(True)

# Adblock
c.content.autoplay= False
c.content.blocking.method = 'both'
c.content.default_encoding = 'utf-8'
c.content.geolocation = False

# Pdfs in qutebrowser
c.content.pdfjs = True

# Binds
config.bind('<Ctrl-=>', 'zoom-in')
config.bind('<Ctrl-->', 'zoom-out')

# Google
c.url.searchengines = {'DEFAULT': 'https://google.com/search?hl=en&q={}'}

# Default page
c.url.start_pages = ['/home/ydvo/.config/qutebrowser/startpage/startpage.html']
c.url.default_page = '/home/ydvo/.config/qutebrowser/startpage/startpage.html'

# Theme
config.source('themes/qute-city-lights/city-lights-theme.py')

# Hint Color
c.colors.hints.bg = 'white'
c.colors.hints.fg = 'black'
c.hints.border = '1px solid #000000'

# Prefer Dark
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.bg = 'black'
