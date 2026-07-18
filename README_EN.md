# Smart Scouting Dashboard

Player performance analysis from the Qatar 2022 World Cup using StatsBomb data and Power BI visualization.

## Description

This project extracts, processes, and visualizes event data from the Qatar 2022 World Cup to facilitate player scouting. A Python script connects to the StatsBomb API, extracts key performance metrics, and generates a consolidated dataset that feeds an interactive dashboard in Power BI.

## Objective

Demonstrate data analysis capabilities applied to football, combining:
- Python programming for data extraction and transformation
- Statistical analysis of player performance
- Interactive visualization for decision-making

## Tech Stack

- **Python 3.10+** - Main processing language
- **Pandas** - Data manipulation and aggregation
- **StatsBombPy** - Football data API connection
- **TQDM** - Progress bar for match processing
- **Power BI** - Visualization and interactive dashboard

## Project Structure

```
smart-scouting-dashboard/
├── extractor_futbol.py          # Data extraction script
├── requirements.txt             # Python dependencies
├── datos/
│   ├── scouting_qatar_2022.csv  # Consolidated player dataset
│   ├── datos_pases_final.csv    # Granular pass data
│   └── README.md                # Data dictionary
├── dashboards/
│   └── screenshots/             # Dashboard screenshots (coming soon)
└── docs/
    └── metodologia.md           # Analysis methodology
```

## How to Run

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/smart-scouting-dashboard.git
cd smart-scouting-dashboard

# Create virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the data extractor
python extractor_futbol.py
```

This will generate the `scouting_qatar_2022.csv` file with updated data.

## Results

The generated dataset contains **653 players** from 32 national teams with the following metrics:

- Passes attempted and completed
- Shots and goals
- Pressures on the opponent
- Dribbles attempted and successful
- Tackles
- Percentage effectiveness

## Dashboard (Power BI)

The `scouting.pbix` file contains an interactive dashboard with:
- Player comparison table
- Filters by team, position, and metrics
- Performance distribution charts

> Dashboard screenshots will be added soon in `dashboards/screenshots/`.

## Next Steps

- [ ] Add Power BI dashboard screenshots
- [ ] Incorporate European league data
- [ ] Add advanced metrics (xA, xG if available)
- [ ] Create interactive version with Streamlit

## Author

Analysis completed as part of **Football Data Analysis and Scouting** training.

## License

This project uses data from StatsBomb under their [open license](https://github.com/statsbomb/open-data).
