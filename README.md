This mini-project simulates cow movement in a simulated break and explores three key KPIs:

1. **Grazing** – % time grazing and grazing density.
2. **DM/kg per cow** – average DM/kg within the simulated pasture.
3. **Night restlessness** – proportion of movement events at night per cow.

**Key Features:**
- **Python:** Simualtes data, analyses data, visualisation.
- **SQL:** Quick query to showcase SQL knowledge.
- **R:** KPI validation and statistical model.
- **Data quality checks:** Identifying gaps, out-of-bounds positions, and anomalies.
- **Communication:** Each KPI includes a short real-world interpretation.

**Structure:**
cow-movement-analyzer/
├─ data/ # Generated data files (ignored in git)
├─ notebooks/ # Analysis notebook & data generator
├─ r/ # Quarto report
├─ requirements.txt # Python dependencies
├─ README.md # This file
├─ _quarto.yml # Quarto config
└─ index.qmd # Landing page for quarto site

## How to run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Generate data and run notebooks in notebooks/.