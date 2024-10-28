# Grand Slam Odds Scraping and Processing

This repository contains two Python scripts designed to streamline the process of scraping and processing ante-post odds data for Grand Slam tournaments. The project is currently set up to handle both WTA and ATP odds data for 23 tournaments spanning from 2019 to 2024, but it can be easily adapted to scrape specific years or tournament types as needed.

## Scripts Overview

1. **scraping.py**  
   - Scrapes ante-post odds from [sportsoddshistory.com](https://www.sportsoddshistory.com) and exports the data into `output.xlsx`.
   - You can customize the script to scrape odds for particular tournaments or specific years, making it adaptable for a wide range of analyses.

2. **modify.py**  
   - Processes `output.xlsx` by removing missing values and converting American odds to decimal odds.
   - Outputs a cleaned dataset in `output2.xlsx`, organized with separate sheets for each tournament scraped.

## Output Structure

The final `output2.xlsx` file will contain individual sheets for each tournament's odds data.
![Output Structure](Images/First.png)

### Further Data Transformation

To evaluate a betting strategy using Elo-based simulation results (e.g., with the [EloMC R package](https://github.com/SaveFonta/EloMC)), additional transformations are required.

#### Final Data Requirements

The expected final structure should resemble:
![Final Structure](Images/Second.png)

### Steps to Transform Data

Follow these steps to prepare the data for use with betting simulations:

1. **Data Preparation in Excel**:
   - Open `output2.xlsx`.
   - Select the first column, go to **Data > Text to Columns**.
   - Click **Next**, check **Space** as the delimiter, then click **Finish**.
   
   ![Data Preparation](Images/Third.png)

2. **Creating Player Column**:
   - Use the following formula in Excel's "Player" column:
     ```excel
     =(IF(D2<>"";D2;IF(C2<>"";C2;IF(B2<>"";B2;"")))) & " " & LEFT(A2;1) & "."
     ```

3. **Adding Results**:
   - Enter "WINNER" in the first row of the "Results" column on each sheet.

Once these steps are completed, `output2.xlsx` will be ready for analysis with functions like `Results_betting` from the EloMC package.

### Pre-Cleaned Data Files

For ease of use, pre-cleaned datasets are also provided:
- **Database Tennis.xlsx** - contains processed odds for ATP tournaments.
- **Final_odds_WTA.xlsx** - contains processed odds for WTA tournaments.

These files are ready for direct use with betting simulations or other analyses.

## Customization Tips

The `scraping.py` script can be easily adjusted to fetch data for selected years or specific tournament types. Simply modify the relevant parameters in the script, and the rest of the processing pipeline will accommodate these changes seamlessly.

---


