from kivy.uix.screenmanager import NoTransition, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
import sys,os,json,requests,certifi

pid=""

#SCREEN MANAGER INSIDE main.kv
#Add Screen to it
#Bandung Software@Soni Ayi Purnama interest to Python Development
from pagedetail.detail import PageDetail

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["ASSET"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["ROOT"] = os.path.dirname(os.path.abspath(__file__))
os.environ["ASSET"] = os.path.join(
    os.environ["ROOT"], f"asset{os.sep}"
)
Window.softinput_mode = "below_target"
os.environ['SSL_CERT_FILE'] = certifi.where()

class Landing(Screen):

    def __init__(self, *args,**kwargs):
        super(Landing, self).__init__(*args,**kwargs)

    def get_data(self):
        f = open("data.json", "rb")
        f_data = f.read().decode()
        data = json.loads(f_data)
        f.close()
        return data

    def set_data(self, key, value):
        data = self.get_data()
        data[key] = value
        f = open("data.json", "wb")
        f.write(json.dumps(data).encode())

    def check_logged(self, *args):
        data = self.get_data()
        if data['logged'] == "True":
            m = self.ids.screen_manager
            m.transition = NoTransition()

            self.ids.screen_manager.current = "main_screen"
            self.enable_drawer()
            m.transition = SlideTransition()

    def enable_drawer(self):
        self.ids.w_toolbar.left_action_items.append(['menu', lambda x: self.ids.nav_drawer.toggle_nav_drawer()])

    def logout(self):
        self.ids.w_toolbar.left_action_items = []
        self.ids.screen_manager.current = 'login_screen'
        self.set_data("logged", "False")

    def navigate_to(self, page,id):
        self.ids.screen_manager.current = page
        if not id is None:
            self.ids.detail_screen.ids.product_id.text=id


    def open_menu(self, *args):
        self.ids.nav_drawer.toggle_nav_drawer()

class ContentNavigationDrawer(BoxLayout):
    nav_drawer = ObjectProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class MainNavigationLayout(NavigationLayout):
    def __init__(self, *args, **kwargs):
        NavigationLayout.__init__(self, *args, **kwargs)
        self._panel_disable = True


class Main(MDApp):
    def __init__(self, *args, **kwargs):
        MDApp.__init__(self, *args, **kwargs)
        self.theme_cls.primary_palette = "Cyan"

    def build(self):
        self.root.check_logged()
Main().run()