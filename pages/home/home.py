import os,json,requests,certifi

from kivy.clock import Clock

from pages.base import BaseScreen
from kivymd.utils.cropimage import crop_image
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.image import Image
from kivymd.uix.imagelist import SmartTileWithLabel
from functools import partial

class Grid(MDGridLayout):
    pass

class PageMainGrid(BaseScreen):
    def __init__(self, *args,**kwargs):
        super(PageMainGrid, self).__init__(*args,**kwargs)

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        """Crop images for Grid screen."""
        if not os.path.exists(
             os.path.join(os.environ["ASSET"], path_to_crop_image)
        ):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace("_tile_crop", "")
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image
        Image(source=instance.source)

        # self.ids..add_widget(img)


    def fetch_data(self,limit):
        if self.ids['fetch_data'].text =="":
            self.ids['grid_list'].clear_widgets()
            payload = {
                'limit': limit,
                'offset': 1
            }
            headers = {
                'Host': 'www.importirjamtangan.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://www.importirjamtangan.com/api/api_front/index',
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
                'Origin': 'https://www.importirjamtangan.com.com',
            }
            r = requests.post('https://importirjamtangan.com/api/api_front/index', data=json.dumps(payload),
                              headers=headers,
                              verify=True)
            data_json = r.json()['data']
            # print(data_json)
            list = []
            for item in data_json:
                row = {"type_id":None,"name": None, "type": None,"image":None}
                row['type_id']=item['type_id']
                row['name'] = item['name']
                row['city'] = item['type']
                row['image']=item['detail'][0]['file']
                # url = f'{environ["ASSET"]}beautiful-931152_1280_tile_crop.png'
                name=row['image'].replace(" ","%20")
                id=row['type_id']
                url='https://importirjamtangan.com/manage/resources/files/' + name
                catalogue=SmartTileWithLabel(source=url, id=row['type_id'], text=row['name'], mipmap=True,
                                       font_style='Subtitle1')
                if not catalogue is None:
                    catalogue.bind(on_release=partial(self.switch_screen,id))
                self.ids['grid_list'].add_widget(catalogue)
                self.ids.fetch_data.text='fetch'
                print(self.ids.fetch_data.text)

                # self.ids['grid_list'].add_widget(SmartTileWithLabel(source=url, id=row['type_id'], text=row['name'], mipmap=True,
                #                        font_style='Subtitle1'))
                # self.ids['grid_list'].bind(on_release="app.root.screen_manager.current=lacak_screen'")

                #dowload file :
                    # urllib.request.urlretrieve(url, f'{environ["ASSET"]}' + name)
                #crop image:
                    # self.crop_image_for_tile(self.ids[id], self.ids[id].size, url)


    def on_enter(self):
        print('User pressed enter in')


    def switch_screen(self,*args,**kwargs):
        self.root.navigate_to("detail_screen",args[0])

        # print(str(args[0]))