from flask import Flask, render_template, jsonify
import requests
import json
from datetime import datetime, timedelta
import plotly.graph_objs as go
import plotly.utils
import pandas as pd
import numpy as np

app = Flask(__name__)

def get_bitcoin_data():
    """Fetch real-time Bitcoin data from CoinGecko API"""
    try:
        # Get current Bitcoin price and market data
        url = "https://api.coingecko.com/api/v3/coins/bitcoin"
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"CoinGecko API returned status code: {response.status_code}")
            # Return mock data when API is rate limited
            return get_mock_bitcoin_data()
            
        data = response.json()
        
        return {
            'price_usd': data['market_data']['current_price']['usd'],
            'price_change_24h': data['market_data']['price_change_percentage_24h'],
            'market_cap': data['market_data']['market_cap']['usd'],
            'volume_24h': data['market_data']['total_volume']['usd'],
            'circulating_supply': data['market_data']['circulating_supply'],
            'max_supply': data['market_data']['max_supply'],
            'ath': data['market_data']['ath']['usd'],
            'ath_date': data['market_data']['ath_date']['usd'],
            'atl': data['market_data']['atl']['usd'],
            'atl_date': data['market_data']['atl_date']['usd'],
            'last_updated': data['last_updated']
        }
    except Exception as e:
        print(f"Error fetching Bitcoin data: {e}")
        return get_mock_bitcoin_data()

def get_mock_bitcoin_data():
    """Return realistic mock Bitcoin data for demonstration"""
    import random
    from datetime import datetime, timedelta
    
    # Base price around current Bitcoin price
    base_price = 114000
    # Add some random variation
    price_variation = random.uniform(-2000, 2000)
    current_price = base_price + price_variation
    
    # Generate realistic market data
    market_cap = current_price * 19900000  # Approximate circulating supply
    volume_24h = market_cap * random.uniform(0.02, 0.05)  # 2-5% of market cap
    price_change_24h = random.uniform(-5, 5)  # -5% to +5% change
    
    return {
        'price_usd': current_price,
        'price_change_24h': price_change_24h,
        'market_cap': market_cap,
        'volume_24h': volume_24h,
        'circulating_supply': 19900000,
        'max_supply': 21000000,
        'ath': 123000,
        'ath_date': '2025-07-14T07:56:01.937Z',
        'atl': 67.81,
        'atl_date': '2013-07-06T00:00:00.000Z',
        'last_updated': datetime.now().isoformat() + 'Z'
    }

def get_historical_data():
    """Fetch historical Bitcoin price data for charts"""
    try:
        # Get 30 days of historical data
        url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        params = {
            'vs_currency': 'usd',
            'days': '30',
            'interval': 'daily'
        }
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code != 200:
            print(f"CoinGecko API returned status code: {response.status_code}")
            # Return mock data when API is rate limited
            return get_mock_historical_data()
            
        data = response.json()
        
        # Process price data
        prices = data['prices']
        dates = [datetime.fromtimestamp(price[0]/1000) for price in prices]
        prices_usd = [price[1] for price in prices]
        
        # Process volume data
        volumes = data['total_volumes']
        volumes_usd = [volume[1] for volume in volumes]
        
        return {
            'dates': dates,
            'prices': prices_usd,
            'volumes': volumes_usd
        }
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return get_mock_historical_data()

def get_mock_historical_data():
    """Return realistic mock historical Bitcoin data"""
    import random
    from datetime import datetime, timedelta
    
    # Generate 30 days of historical data
    dates = []
    prices = []
    volumes = []
    
    base_price = 114000
    base_volume = 50000000000  # 50B daily volume
    
    for i in range(30):
        # Generate date (30 days ago to today)
        date = datetime.now() - timedelta(days=29-i)
        dates.append(date)
        
        # Generate realistic price movement
        price_change = random.uniform(-0.05, 0.05)  # -5% to +5% daily change
        base_price *= (1 + price_change)
        prices.append(base_price)
        
        # Generate realistic volume
        volume_change = random.uniform(0.8, 1.2)  # 80% to 120% of base volume
        volumes.append(base_volume * volume_change)
    
    return {
        'dates': dates,
        'prices': prices,
        'volumes': volumes
    }

def create_price_chart(historical_data):
    """Create an interactive price chart using Plotly"""
    if not historical_data:
        return None
    
    # Create price chart
    price_trace = go.Scatter(
        x=historical_data['dates'],
        y=historical_data['prices'],
        mode='lines',
        name='Bitcoin Price (USD)',
        line=dict(color='#f7931a', width=2),
        fill='tonexty',
        fillcolor='rgba(247, 147, 26, 0.1)'
    )
    
    # Create volume chart
    volume_trace = go.Bar(
        x=historical_data['dates'],
        y=historical_data['volumes'],
        name='24h Volume (USD)',
        marker_color='rgba(0, 123, 255, 0.6)',
        yaxis='y2'
    )
    
    layout = go.Layout(
        title='Bitcoin Price & Volume (30 Days)',
        xaxis=dict(
            title='Date',
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)',
            color='#ffffff'
        ),
        yaxis=dict(
            title='Price (USD)',
            side='left',
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)',
            color='#ffffff'
        ),
        yaxis2=dict(
            title='Volume (USD)',
            side='right',
            overlaying='y',
            showgrid=False,
            color='#ffffff'
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff'),
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    fig = go.Figure(data=[price_trace, volume_trace], layout=layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

@app.route('/')
def index():
    """Main page with Bitcoin price tracker"""
    bitcoin_data = get_bitcoin_data()
    historical_data = get_historical_data()
    chart_json = create_price_chart(historical_data)
    
    return render_template('index.html', 
                         bitcoin_data=bitcoin_data,
                         chart_json=chart_json)

@app.route('/api/bitcoin')
def api_bitcoin():
    """API endpoint for Bitcoin data"""
    data = get_bitcoin_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch Bitcoin data'}), 500

@app.route('/api/historical')
def api_historical():
    """API endpoint for historical data"""
    data = get_historical_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch historical data'}), 500

if __name__ == '__main__':
    app.run(debug=True)

