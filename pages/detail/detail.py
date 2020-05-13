from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage
from pages.base import BaseScreen
import requests,json,certifi


class PageDetail(BaseScreen):
    # def __init__(self,**kwargs):
    #     super().__init__(**kwargs)

    def on_enter(self):
        if (not self.ids.fetch_id.text is None) and self.ids.fetch_id.text==self.ids.product_id.text:
            print('fetch_id' + self.ids.fetch_id.text)
            print('product_id'+ self.ids.product_id.text)

        else:
            self.ids['detail_layout'].clear_widgets()
            self.ids.fetch_id.text=self.ids.product_id.text
            self.fetch_data()

    def fetch_data(self):
        #getting data from label with ofacity->0
        #Cause dificult to sending parameter between page/screen
        product_id=self.ids.product_id.text
        #Dont Call Request Before Call
        if not product_id is None:
            payload = {
                'keyword': product_id
            }
            headers = {
                'Host': 'www.importirjamtangan.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://www.importirjamtangan.com/api/api_checkout/index',
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
                'Origin': 'https://www.importirjamtangan.com.com',
            }
            r = requests.post('https://importirjamtangan.com/api/api_checkout/index', data=json.dumps(payload),
                              headers=headers,
                              verify=True)
            data_json = r.json()['data']
            print(data_json)
            list = []
            for item in data_json:
                row = {"type_id": None, "name": None, "type": None, "image": None}
                row['type_id'] = item['type_id']
                row['name'] = item['name']
                row['city'] = item['type']
                row['image'] = item['detail'][0]['file']
                # url = f'{environ["ASSET"]}beautiful-931152_1280_tile_crop.png'
                name = row['image'].replace(" ", "%20")
                id = row['type_id']
                url = 'https://importirjamtangan.com/manage/resources/files/' + name
            self.ids.detail_layout.add_widget(AsyncImage(source=url))

class Tracking(BoxLayout):
    pass


