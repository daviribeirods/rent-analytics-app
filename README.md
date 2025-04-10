# RentPrice Brasília

A web application built with Dash to analyze and visualize rental prices in Brasília for the year 2025.

## Overview

RentPrice Brasília is a data visualization dashboard that helps users understand rental market trends in Brasília. The application features a modern, responsive interface built with Dash and Bootstrap components.

## Project Structure

```
rentprice-brasilia/
├── app/
│   ├── app.py             # Main application file with core setup
│   ├── pages/             # Multi-page components
│   │   ├── home.py       # Home page
│   │   └── about.py      # About page
│   └── assets/           # Static files (CSS, images)
```

## Features (v1.0.0)

- Multi-page application with responsive layout
- Bootstrap-based UI with COSMO theme
- Three main sections:
  - Home: Overview and main metrics
  - About: Project information and methodology
- Data from DF Móveis website

## Future versions

- Analytics: Detailed data visualizations
- Add: Integration with other data sources
- Add: Machine learning models to predict rental prices
- Add: LLMs to answer questions about rental prices

## Tech Stack

- Python
- Dash
- Dash Bootstrap Components
- Plotly (for visualizations)

## Getting Started

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the application:
```bash
python app/app.py
```
4. Open your browser and navigate to `http://localhost:8050`

## Contributing

Feel free to open issues and pull requests for any improvements.
