import requests
import os

def download_nasa_data():
    url= "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
    response=requests.get(url)
    if response.status_code==200:
        print("NASA GISS was successfully contacted.")
        os.makedirs("data/raw", exist_ok=True)
        filepath=os.path.join("data","raw","nasa_giss_temperature.csv")
        with open(filepath,"wb") as f:
            f.write(response.content)
        print(f"The file is saved in: {filepath}")
    else:
        print(f"Loading failed. Status code: {response.status_code}")
def download_owid_data():
    url="https://ourworldindata.org/grapher/annual-co2-emissions-per-country.csv?v=1&csvType=full&useColumnShortNames=true"
    response=requests.get(url)
    if response.status_code==200:
        print("OWID was successfully contacted.")
        os.makedirs("data/raw", exist_ok=True)
        filepath=os.path.join("data","raw","owid_annual_co2_emissions.csv")
        with open(filepath,"wb") as f:
            f.write(response.content)
        print(f"The file is saved in: {filepath}")
    else:
        print(f"Loading failed. Status code: {response.status_code}") 
def  download_country_classification():
    url="https://ddh-openapi.worldbank.org/resources/DR0095334/download"
    response=requests.get(url)
    if response.status_code==200:
        print("worldbank was successfully contacted.")
        os.makedirs("data/raw", exist_ok=True)
        filepath=os.path.join("data", "raw", "country_classification_raw.xlsx")
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"The file is saved in: {filepath}")
    else:
        print(f"Loading failed. Status code: {response.status_code}") 
def download_renewable_energy_data():
    url="https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.csv"
    response=requests.get(url)
    if response.status_code==200:
        print("OWID  was successfully contacted.")
        os.makedirs("data/raw", exist_ok=True)
        filepath=os.path.join("data", "raw", "renewable_energy_raw.csv")
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"The file is saved in: {filepath}")
    else:
        print(f"Loading failed. Status code: {response.status_code}") 
if __name__ == "__main__":
    #download_nasa_data()
    #download_owid_data()
    #download_country_classification()
    download_renewable_energy_data()
