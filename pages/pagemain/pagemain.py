import sys,os,json,requests,ast
from pages.base import BaseScreen
from kivymd.utils.cropimage import crop_image
from os import environ
from KivyMD.kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.image import Image

class Grid(MDGridLayout):
    pass

class PageMainGrid(BaseScreen):
    def __init__(self, *args,**kwargs):
        super(PageMainGrid, self).__init__(*args,**kwargs)
        # self.fetch_data_from_database()
        # print(self.ids['grid'])

    def crop_image(self):
        self.crop_image_for_tile(self.ids.tile_1,self.ids.tile_1.size, f'{environ["ASSET"]}beautiful-931152_1280_tile_crop.png')
        self.crop_image_for_tile(self.ids.tile_2,self.ids.tile_2.size, f'{environ["ASSET"]}african-lion-951778_1280_tile_crop.png')
        self.crop_image_for_tile(self.ids.tile_3,self.ids.tile_3.size, f'{environ["ASSET"]}guitar-1139397_1280_tile_crop.png')
        self.crop_image_for_tile(self.ids.tile_4,self.ids.tile_4.size, f'{environ["ASSET"]}robin-944887_1280_tile_crop.png')
        self.crop_image_for_tile(self.ids.tile_5,self.ids.tile_5.size, f'{environ["ASSET"]}kitten-1049129_1280_tile_crop.png')
        self.crop_image_for_tile(self.ids.tile_6,self.ids.tile_6.size, f'{environ["ASSET"]}light-bulb-1042480_1280_tile_crop.png')

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        """Crop images for Grid screen."""
        if not os.path.exists(
             os.path.join(os.environ["ASSET"], path_to_crop_image)
        ):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace("_tile_crop", "")
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image
        img = Image(source=instance.source)
        self.ids.tile_1.add_widget(img)

    #here the problem
    def fetch_data_from_database(self):
        payload = {
            'limit': 3,
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
            row = {"name": None, "type": None,"image":None}
            row['name'] = item['name']
            row['city'] = item['type']
            row['image']=item['detail'][0]['file']

            # SmartTileWithLabel:
            # id: tile_4
            # mipmap: True
            # text: "Robin\n[size=12]robin-944887_1280.png[/size]"
            # font_style: 'Subtitle1'
            list.append(row)
