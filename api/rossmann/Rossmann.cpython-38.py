import pickle
import os

class MyClass:
    def __init__(self):
        try:
            self.promo2_time_week_rs = self.load_pickle("promo_time_week_rs.pkl")
            self.promo2_time_month_rs = self.load_pickle("promo_time_month_rs.pkl")
            self.competition_distance_yeojohn = self.load_pickle("competition_distance_yeojohn.pkl")
            self.customers_yeojohn = self.load_pickle("customers_yeojohn.pkl")
            self.competition_since_month_yeojohn = self.load_pickle("competition_since_month_yeojohn.pkl")
            self.year_mms = self.load_pickle("year_mms.pkl")
            self.store_type_le = self.load_pickle("store_type_le.pkl")
            self.competition_open_since_year_le = self.load_pickle("competition_open_since_year_le.pkl")
        except Exception as e:
            print(f"Error initializing class: {e}")

    def load_pickle(self, filename):
        filepath = f"C:\\Users\\user\\Desktop\\Git_Folder\\Rossmann-Store-Sales-\\api\\rossmann\\__pycache__\\{filename}"
        if os.path.exists(filepath):
            with open(filepath, "rb") as file:
                return pickle.load(file)
        else:
            raise FileNotFoundError(f"File {filepath} not found.")
