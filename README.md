# Smart Energy Intelligence System

A simple AI prototype for detecting unusual electricity consumption.

## Workflow
Energy consumption data -> preprocessing -> Isolation Forest -> anomaly detection -> investigation

## AI technique
Isolation Forest is an unsupervised machine-learning algorithm that identifies unusual observations.

## Important note
The included readings are illustrative/sample data created for demonstration, not measurements from a real building.

## Run
```bash
pip install -r requirements.txt
python energy_anomaly.py
```

## Limitation
Aggregate meter data can identify unusual time periods, but cannot identify the exact appliance responsible without appliance-level data.
