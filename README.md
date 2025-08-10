This mini-project aims to showcase my python / jupyter skills, and my ability to use R & SQL.

KPIs used:
1. **Grazing** – % time grazing and grazing density.
2. **DM/kg per cow** – average DM/kg within the simulated pasture.
3. **Night restlessness** – proportion of movement events at night per cow.
4. **Move speed** - The average movement speeds of each cow.


**Key Features:**
- **Python:** Simulates data
- **Jupyter:** Analyzes and visualises data
- **SQL:** Quick query to showcase SQL knowledge.
- **R:** Shows grazing status per hour of the day.
- **Data quality checks:** Identifying gaps, out-of-bounds positions, and anomalies.
- **Communication:** Each KPI includes a short real-world interpretation.

**Assumptions:**
Assumptions made for this showcase (not applicable in real-world scenarios):
- All areas of the paddock are equal for grazing
- Any time a cow is travelling less than 0.06m/s then it is grazing (even when asleep)
- DM Intake rate per cow is 0.03kg/minute always when grazing

**Further insights:**
The sample I've generated for this is exclusively cow movement data, and would require additional data for better insights.
- DM/kg is measured per cow based on an intake rate, but could be measured per paddock with data on intake rates across different paddocks
- Grazing patterns could be analyzed with data on paddock
- 

**Outliers:**
I've added some simulations of outlier data to show that I've considered these, but they're insignificant in terms of the overall dataset. 
- Cow speed beyond biological capability - could showcase tracker malfunction.
- Long gaps between data points - could indicate incomplete data if persistent.

