import os
from typing import Dict, List
import requests
from dotenv import load_dotenv
from sodapy import Socrata
import pandas as pd
from datetime import datetime

load_dotenv()

class DataGovCollector:
    def __init__(self):
        self.api_key = os.getenv('DATA_GOV_API_KEY')
        self.client = Socrata("data.gov", self.api_key)
        
    def fetch_tech_initiatives(self) -> pd.DataFrame:
        """Fetch technology initiatives and implementation data from data.gov"""
        try:
            # Example dataset IDs - you'll need to replace with actual relevant datasets
            datasets = {
                'it_spending': 'h99c-e2xn',  # IT Dashboard dataset
                'digital_services': 'x97u-rdwj',  # Digital services usage
            }
            
            results = []
            for category, dataset_id in datasets.items():
                data = self.client.get(dataset_id, limit=10000)
                if data:
                    df = pd.DataFrame.from_records(data)
                    df['category'] = category
                    results.append(df)
            
            return pd.concat(results) if results else pd.DataFrame()
        
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return pd.DataFrame()

    def fetch_performance_metrics(self) -> pd.DataFrame:
        """Fetch government performance metrics related to technology"""
        try:
            # Example endpoint for performance.gov API
            url = "https://api.performance.gov/data/technology-metrics"
            headers = {"X-Api-Key": self.api_key}
            
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return pd.DataFrame(response.json())
            return pd.DataFrame()
            
        except Exception as e:
            print(f"Error fetching performance metrics: {str(e)}")
            return pd.DataFrame()

    def save_data(self, df: pd.DataFrame, category: str):
        """Save collected data to CSV"""
        if not df.empty:
            timestamp = datetime.now().strftime("%Y%m%d")
            filename = f"data/raw/{category}_{timestamp}.csv"
            df.to_csv(filename, index=False)
            print(f"Saved {category} data to {filename}")
