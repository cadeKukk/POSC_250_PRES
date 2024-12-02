import pandas as pd
import requests
from typing import Dict, List, Optional
from datetime import datetime

class WorldBankCollector:
    def __init__(self):
        self.base_url = "https://api.worldbank.org/v2"
        
    def fetch_digital_adoption_index(self, year_start: int = 2016) -> pd.DataFrame:
        """
        Fetch Digital Adoption Index (DAI) data from World Bank
        DAI measures countries' digital adoption across three dimensions:
        people, government, and business
        """
        try:
            # World Bank API endpoint for Digital Adoption Index
            endpoint = f"{self.base_url}/country/all/indicator/IE.DAI.GOVT.XQ"
            params = {
                "format": "json",
                "date": f"{year_start}:{datetime.now().year}",
                "per_page": 1000
            }
            
            response = requests.get(endpoint, params=params)
            if response.status_code == 200:
                data = response.json()[1]  # World Bank API returns metadata in [0]
                df = pd.DataFrame(data)
                return df
            return pd.DataFrame()
            
        except Exception as e:
            print(f"Error fetching World Bank DAI data: {str(e)}")
            return pd.DataFrame()
    
    def fetch_government_effectiveness(self, year_start: int = 2016) -> pd.DataFrame:
        """
        Fetch Government Effectiveness indicators
        Measures quality of public services, civil service, policy implementation
        """
        try:
            endpoint = f"{self.base_url}/country/all/indicator/GE.EST"
            params = {
                "format": "json",
                "date": f"{year_start}:{datetime.now().year}",
                "per_page": 1000
            }
            
            response = requests.get(endpoint, params=params)
            if response.status_code == 200:
                data = response.json()[1]
                df = pd.DataFrame(data)
                return df
            return pd.DataFrame()
            
        except Exception as e:
            print(f"Error fetching government effectiveness data: {str(e)}")
            return pd.DataFrame()
    
    def save_data(self, df: pd.DataFrame, category: str):
        """Save collected data to CSV"""
        if not df.empty:
            timestamp = datetime.now().strftime("%Y%m%d")
            filename = f"data/raw/worldbank_{category}_{timestamp}.csv"
            df.to_csv(filename, index=False)
            print(f"Saved World Bank {category} data to {filename}")
