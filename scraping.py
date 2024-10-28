import pandas as pd

# Lista URL per ciascun torneo e anno, for women, just change in each line "m&o" with "w&o"
urls = {
    'Australian Open': [
        "https://www.sportsoddshistory.com/tennis-main/?y=2024&sa=tennis&x=m&a=aus&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2023&sa=tennis&a=aus&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2022&sa=tennis&a=aus&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2021&sa=tennis&a=aus&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2020&sa=tennis&a=aus&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2019&sa=tennis&a=aus&x=m&o=r"
    ],
    'French Open': [
        "https://www.sportsoddshistory.com/tennis-main/?y=2024&sa=tennis&a=french&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2023&sa=tennis&a=french&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2022&sa=tennis&a=french&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2021&sa=tennis&a=french&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2020&sa=tennis&a=french&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2019&sa=tennis&a=french&x=m&o=r"
    ],
    'Wimbledon': [
        "https://www.sportsoddshistory.com/tennis-main/?y=2024&sa=tennis&x=m&a=wimb&o=r"
        "https://www.sportsoddshistory.com/tennis-main/?y=2023&sa=tennis&a=wimb&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2022&sa=tennis&a=wimb&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2021&sa=tennis&x=m&a=wimb&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2019&sa=tennis&x=m&a=wimb&o=r"  # No 2020
    ],
    'US Open': [
        #https://www.sportsoddshistory.com/tennis-main/?y=2023&sa=tennis&a=us&x=m&o=r STILL NOT AVAILABLE
        "https://www.sportsoddshistory.com/tennis-main/?y=2023&sa=tennis&a=us&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2022&sa=tennis&a=us&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2021&sa=tennis&a=us&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2020&sa=tennis&a=us&x=m&o=r",
        "https://www.sportsoddshistory.com/tennis-main/?y=2019&sa=tennis&a=us&x=m&o=r"
    ]
}

# Nome del file Excel di output
output_file = "output.xlsx"

# Con pd.ExcelWriter si pu scrivere nei fogli di un excel 
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    # Ciclo per iterare attraverso ogni torneo
    for tournament, urls_list in urls.items():
        for url in urls_list:
            
            #In sto modo splittiamo gli utl seguendo gli uguale
            year = url.split('=')[1][:-3]
            
           
            page = pd.read_html(url)

            if tournament == "Australian Open" or tournament == "French Open":
                df = page[1]  
            else:
                df = page [0]
            
            sheet_name = f"{tournament} {year}"
            
            df.to_excel(writer, sheet_name=sheet_name, index=True)
            print(f"Scraping completato per {tournament} - Anno {year}")

print("Operazione completata.")