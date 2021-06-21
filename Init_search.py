from selenium import webdriver
from Page_objects.HomePage import FirstPage

path = "C:\\Users\\calvi\\PycharmProjects\\Webscraping\\tankprijzen\\Drivers\\chromedriver.exe"


class InitiateSearch:
    def __init__(self, location, fuel_type, usage, amount, distance_km):
        self.location = location
        self.fuel_type = fuel_type
        self.usage = usage
        self.fuel_amount = amount
        self.distance_km = distance_km

    def find_station(self):
        driver = webdriver.Chrome(path)
        homepage = FirstPage(driver)
        homepage.search_for_place(self.location)
        homepage.select_fuel_type(self.fuel_type)
        homepage.fill_car_fuel_usage(self.usage)
        homepage.fill_liters_amount_of_fuel(self.fuel_amount)
        homepage.fill_max_distance_to_station_km(self.distance_km)
        homepage.click_search_button()
        homepage.click_first_option()
        text = homepage.get_information_from_page()
        driver.close()
        return text
