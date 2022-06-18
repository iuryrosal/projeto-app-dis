from bs4 import BeautifulSoup
import requests

class WebScraping:
    def __init__(self, url):
        self.url = url
        self.soup = self.__get_html()
    
    def __get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup
    
    def __get_rooms(self):
        return self.soup.find_all("div", class_ = "c4mnd7m dir dir-ltr")
    
    def __get_title(self, room):
        return room.find("div", class_="t1jojoys dir dir-ltr").text

    def __get_beds(self, room):
        attr_room = {}
        details = room.find("div", class_="f15liw5s s1cjsi4j dir dir-ltr")
        beds = details.find("span", class_="dir dir-ltr").text
        return beds

    def __get_price(self, room_html):
        return room_html.find("div", class_ = "p1v28t5c dir dir-ltr").find("span", class_ = "a8jt5op dir dir-ltr").text[2:]
    
    def pick_all_rooms(self):
        list_of_rooms = []
        for room in self.__get_rooms():
            room_info = {}

            room_info["Title"] = self.__get_title(room)
            room_info["Price per Night (R$)"] = self.__get_price(room)
            room_info["Beds"] = self.__get_beds(room)

            list_of_rooms.append(room_info)
        
        return list_of_rooms