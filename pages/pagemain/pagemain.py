import os,requests
from pages.base import BaseScreen
from kivymd.utils.cropimage import crop_image


class PageMainGrid(BaseScreen):
    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        """Crop images for Grid screen."""
        print(os.path)
        if not os.path.exists(
             os.path.join(os.environ["KITCHEN_SINK_ASSETS"], path_to_crop_image)

        ):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace("_tile_crop", "")
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image

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