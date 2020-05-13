from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition, SlideTransition
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
import os,json,sys
from kivy.clock import Clock
<<<<<<< HEAD
from urllib.request import urlopen

#SCREEN MANAGER INSIDE main.kv
#Add Screen to it
#Bandung Software@Soni Ayi Purnama interest to Python Development
# from detail.detail import PageDetail

=======
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.imagelist import SmartTileWithLabel
from functools import partial

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["IMP_ROOT"] = sys._MEIPASS
else:
    os.environ["IMP_ROOT"] = os.path.dirname(os.path.abspath(__file__))

>>>>>>> 58df59f4277fc1e7cd20703e170e04bc205dab7c
Window.softinput_mode = "below_target"

# os.environ['SSL_CERT_FILE'] = certifi.where()

<<<<<<< HEAD
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     # Clock.schedule_once(self.check_logged)
    def internet_on(self):
        try:
            response = urlopen('https://www.importirjamtangan.com/', timeout=10)
            print('good connection')
            return True
        except:
            return False
=======
class Landing(Screen):
>>>>>>> 58df59f4277fc1e7cd20703e170e04bc205dab7c

    def get_data(self):
        f = open(f"{os.environ['IMP_ROOT']}/data.json", "rb")
        f_data = f.read().decode()
        data = json.loads(f_data)
        f.close()
        return data

    def set_data(self, key, value):
        data = self.get_data()
        data[key] = value
        f = open(f"{os.environ['IMP_ROOT']}/data.json", "wb")
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._panel_disable = True

<<<<<<< HEAD

class Main(MDApp):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        if self.root.internet_on()==True:
            Clock.schedule_once(self.root.check_logged)
        else:
            self.root.ids.screen_manager.current = "no_conn"

if __name__=="__main__":
    Main().run()
=======
#home page
class Grid(MDGridLayout):
    pass

class PageHome(Landing):
    def fetch_data(self,limit,query):
        pass
    # def fetch_data(self,limit,query):
    #     # print(self.parent.parent.parent.ids['grid_list'])
    #     self.parent.parent.parent.ids['grid_list'].clear_widgets()
    #     if query is None:
    #         payload = {
    #             'limit': limit,
    #             'offset': 1
    #         }
    #     elif not query is None:
    #         payload = {
    #             'limit': limit,
    #             'offset': 1,
    #             'query':query
    #         }
    #     headers = {
    #         'Host': 'www.importirjamtangan.com',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    #         'Accept': 'application/json, text/javascript, */*; q=0.01',
    #         'Accept-Language': 'en-US,en;q=0.5',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Referer': 'https://www.importirjamtangan.com/api/api_product/index',
    #         'Content-Type': 'application/json',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Connection': 'keep-alive',
    #         'Origin': 'https://www.importirjamtangan.com.com',
    #     }
    #     r = requests.post('https://importirjamtangan.com/api/api_product/index', data=json.dumps(payload),
    #                       headers=headers,
    #                       verify=True)
    #     if r.status_code==200:
    #         data_json = r.json()['data']
    #         for item in data_json:
    #             row = {"type_id":None,"name": None, "type": None,"image":None}
    #             row['type_id']=item['type_id']
    #             row['name'] = item['name']
    #             row['city'] = item['type']
    #             row['image']=item['detail'][0]['file']
    #             # url = f'{environ["ASSET"]}beautiful-931152_1280_tile_crop.png'
    #             name=row['image'].replace(" ","%20")
    #             id=row['type_id']
    #             url='https://importirjamtangan.com/manage/resources/files/' + name
    #             catalogue=SmartTileWithLabel(source=url, id=row['type_id'], text=row['name'], mipmap=True,
    #                                    font_style='Subtitle1')
    #             if not catalogue is None:
    #                 catalogue.bind(on_release=partial(self.switch_screen,id))
    #             self.parent.parent.parent.ids['grid_list'].add_widget(catalogue)
    #
    #             # self.ids['grid_list'].add_widget(SmartTileWithLabel(source=url, id=row['type_id'], text=row['name'], mipmap=True,
    #             #                        font_style='Subtitle1'))
    #             # self.ids['grid_list'].bind(on_release="app.root.screen_manager.current=lacak_screen'")
    #
    #             #dowload file :
    #                 # urllib.request.urlretrieve(url, f'{environ["ASSET"]}' + name)
    #             #crop image:
    #                 # self.crop_image_for_tile(self.ids[id], self.ids[id].size, url)
    #     elif r.status_code==400:
    #         pass
    #     elif r.status_code==500:
    #         pass
    #     # else:
    #     #     self.root.navigate_to("no_conn")

    def on_text_validate(self):
        query=self.ids.search_text.text
        self.fetch_data(6,query)
    def switch_screen(self,*args,**kwargs):
        self.parent.parent.parent.navigate_to("detail_screen",args[0])
        # print(str(args[0]))
#End Home Screen

#Login Page
class PageLogin(Screen):
    email = ObjectProperty()
    password = ObjectProperty()

    def loggin_user(self):
        if self.email.text == '1' and self.password.text == '1':
            self.parent.parent.parent.navigate_to("main_screen",None)
            self.enable_nav()
            self.parent.parent.parent.set_data("logged", "True")

    def enable_nav(self):
            menu = ["menu", self.parent.parent.parent.open_menu]
            self.parent.parent.parent.ids.w_toolbar.left_action_items.append(menu)

class ImportirApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Cyan"

    def on_start(self):
        Clock.schedule_once(self.root.check_logged)

    def build(self):
        return Builder.load_file(
            f"{os.environ['IMP_ROOT']}/main.kv"
        )


#End Login Page
# if __name__=="__main__":
ImportirApp().run()
>>>>>>> 58df59f4277fc1e7cd20703e170e04bc205dab7c
