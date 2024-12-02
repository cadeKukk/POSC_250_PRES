import os
import sys

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.collectors.data_gov_collector import DataGovCollector
from src.collectors.world_bank_collector import WorldBankCollector
from src.collectors.un_egov_collector import UNEGovCollector
from datetime import datetime
import pandas as pd

def main():
    # Initialize collectors
    data_gov = DataGovCollector()
    world_bank = WorldBankCollector()
    un_egov = UNEGovCollector()
    
    print("Starting data collection process...")
    
    # Collect US government data
    tech_data = data_gov.fetch_tech_initiatives()
    if not tech_data.empty:
        data_gov.save_data(tech_data, "tech_initiatives")
        print(f"Collected {len(tech_data)} technology implementation records")
    
    metrics_data = data_gov.fetch_performance_metrics()
    if not metrics_data.empty:
        data_gov.save_data(metrics_data, "performance_metrics")
        print(f"Collected {len(metrics_data)} performance metric records")
    
    # Collect World Bank data
    dai_data = world_bank.fetch_digital_adoption_index()
    if not dai_data.empty:
        world_bank.save_data(dai_data, "digital_adoption_index")
        print(f"Collected {len(dai_data)} Digital Adoption Index records")
    
    gov_eff_data = world_bank.fetch_government_effectiveness()
    if not gov_eff_data.empty:
        world_bank.save_data(gov_eff_data, "government_effectiveness")
        print(f"Collected {len(gov_eff_data)} Government Effectiveness records")
    
    # Collect UN E-Government data
    egdi_data = un_egov.fetch_egov_development_index()
    if not egdi_data.empty:
        un_egov.save_data(egdi_data, "egov_development_index")
        print(f"Collected {len(egdi_data)} E-Government Development Index records")
    
    print("Data collection completed")

if __name__ == "__main__":
    main()
