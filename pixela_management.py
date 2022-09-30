import requests
from datetime import datetime

# TODO 1: Create update pixel method
# TODO 2: Create delete pixel method
# TODO 4: Create a create user class
# TODO 5: Managing user information method?


class PixelaManager:

    def __init__(self):
        self.USERNAME = "<username>"
        self.PX_TOKEN = "<Your Token>"
        self.GRAPH_ID = "<graph id>"
        self.PIXELA_ROOT_ENDPOINT = "https://pixe.la/v1/users"
        self.HEADERS = {"X-USER-TOKEN": self.PX_TOKEN}

    def post_pixel(self, quantity: str):
        """Enter quantity as string. Use get_graph_def method for graph input definitions.
        Refer to Pixela documentation for further information
        https://docs.pixe.la/entry/post-pixel"""

        today = datetime.now()
        today_formatted = today.strftime("%Y%m%d")

        pixel_params = {
            "date": today_formatted,
            "quantity": quantity
        }
        pixel_endpoint = f"{self.PIXELA_ROOT_ENDPOINT}/{self.USERNAME}/graphs/{self.GRAPH_ID}"
        response = requests.post(url=pixel_endpoint, json=pixel_params, headers=self.HEADERS)
        print(response.text)

    def delete_pixel(self, date: str):
        """Enter pixel date as 'YYYYmmdd' as a string.
        Refer to Pixela documentation for further information
        https://docs.pixe.la/entry/delete-pixel"""

        pixel_del_endpoint = f"{self.PIXELA_ROOT_ENDPOINT}/{self.USERNAME}/graphs/{self.GRAPH_ID}/{date}"
        response = requests.delete(url=pixel_del_endpoint, headers=self.HEADERS)
        print(response.text)

    def update_pixel(self, new_quantity: str, date: str):
        """Enter new quantity as string. Enter date YYYYmmdd as string.
        Refer to Pixela documentation for further information
        https://docs.pixe.la/entry/put-pixel"""

        pixel_del_endpoint = f"{self.PIXELA_ROOT_ENDPOINT}/{self.USERNAME}/graphs/{self.GRAPH_ID}/{date}"
        pixel_params = {
            "quantity": new_quantity
        }
        response = requests.put(url=pixel_del_endpoint, json=pixel_params, headers=self.HEADERS)
        print(response.text)

    def get_graph_def(self):
        get_g_endpoint = f"{self.PIXELA_ROOT_ENDPOINT}/{self.USERNAME}/graphs"
        response = requests.get(url=get_g_endpoint, headers=self.HEADERS)
        print(response.text)

    def create_graph(self, g_parameters: dict):
        """Enter graph parameters as a dictionary. Keys are
        id: <graphid>,
        name: <Graph Name>,
        unit: <Measurement Units>,
        type: <int or float>,
        color: <Graph Color>
        Refer to Pixela documentation for details on parameters
        https://docs.pixe.la/entry/post-graph"""

        graph_endpoint = f"{self.PIXELA_ROOT_ENDPOINT}/{self.USERNAME}/graphs"
        response = requests.post(url=graph_endpoint, json=g_parameters, headers=self.HEADERS)
        print(response.text)

    def create_user(self, user_parameters: dict):
        """Enter new user parameters as a dictionary. Keys are
        token: <new user token>,
        username: <new username>,
        agreeTermsOfService: <yes / no>,
        notMinor: <yes / no>
        Refer to Pixela documentation for further information on parameters
        https://docs.pixe.la/entry/post-user"""

        response = requests.post(url=self.PIXELA_ROOT_ENDPOINT, json=user_parameters)
        print(response.text)
