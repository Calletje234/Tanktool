from SeleniumHelpers.SeleniumHelpers import SeleniumHelpers


class FirstPage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumHelpers(driver)

    def search_for_place(self, location):
        self.driver.get("http://www.tankje.nl")
        self.selenium.send_tekst("id", location, "tags")

    def select_fuel_type(self, fuel_type):
        fuel_type = fuel_type.lower()
        fuel_type = fuel_type.capitalize()

        if fuel_type != "Lpg":
            self.selenium.click("xpath", f"//input[@value='{fuel_type}']")
        elif fuel_type == "Lpg":
            fuel_type = fuel_type.upper()
            self.selenium.click("xpath", f"//input[@value='{fuel_type}']")
        elif fuel_type != "Lpg" and fuel_type != "Euro 95" and fuel_type != "Diesel" and fuel_type != "Super":
            raise ValueError(f"fuel type: {fuel_type} isn't recognized as a viable option please")

    def fill_car_fuel_usage(self, car_usage):
        self.selenium.send_tekst("name", car_usage, "VERBRUIK")

    def fill_liters_amount_of_fuel(self, amount_liters):
        self.selenium.send_tekst("name", amount_liters, "INHOUD")

    def fill_max_distance_to_station_km(self, amount_km):
        self.selenium.send_tekst("name", amount_km, "AFSTAND")

    def click_search_button(self):
        self.selenium.click("name", "ZOEK")

    def click_first_option(self):
        self.selenium.click("xpath", "//td[@class='ContentTable'][1]//a")

    def get_information_from_page(self):
        text = self.selenium.get_text("xpath", "//td[2][@class='bodyText']")
        return text




