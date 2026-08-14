# NASA Earthdata & POWER Portals Data Extraction

## Overview
Programmatic extraction and inspection of terrestrial temperature records using the NASA POWER API (Hourly API v2.9.5) and Python.

## Technical Details
- **Data Source**: MERRA-2 (GMAO MERRA-2)
- **Community**: Sustainable Buildings (SB)
- **Parameter**: Temperature at 2 Meters (`T2M`) in °C
- **Coordinates**: Latitude `37.1°N`, Longitude `-76.39°W`, Elevation `6.58m`
- **Timeframe**: Jan 1, 2024 – Dec 31, 2024 (LST)

## Execution
Run `nasa_power_api.py` or open the notebook in Google Colab to query the API endpoint and parse the hourly JSON payload.
