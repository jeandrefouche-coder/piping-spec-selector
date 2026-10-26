# Amplats Piping Spec Selector

Interactive Streamlit app to select the correct Amplats (Anglo American Platinum) Pipe Material Specification based on commodity, material, and rating.

## Features
- Dropdown filters for Commodity / Service, Material Type, and Pressure Rating
- Keyword search
- Instant matching results with expandable details
- Full database view

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud
1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo and deploy

## Data source
Extracted from issued Amplats master specifications (APP001 series).  
Always cross-check final selections against the full specification documents.
