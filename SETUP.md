# Bitcoin Price Tracker - Quick Setup Guide

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python3 app.py
   ```

3. **Open your browser:**
   ```
   http://localhost:8080
   ```

## ✅ What's Working

- ✅ Real-time Bitcoin price display
- ✅ Interactive price charts with Plotly
- ✅ Market statistics (market cap, volume, supply)
- ✅ Responsive design for all devices
- ✅ Auto-refresh every 30 seconds
- ✅ Manual refresh button
- ✅ API endpoints for data access
- ✅ Fallback mock data when API is rate limited

## 🌐 API Endpoints

- `GET /` - Main web interface
- `GET /api/bitcoin` - Current Bitcoin data
- `GET /api/historical` - 30-day historical data

## 📊 Features

### Real-time Data
- Live Bitcoin price updates
- 24-hour price change percentage
- Market capitalization
- Trading volume
- Circulating supply information

### Interactive Charts
- 30-day price history
- Volume data overlay
- Responsive chart design
- Hover tooltips

### Modern UI
- Bootstrap 5 framework
- Custom CSS with gradients
- Font Awesome icons
- Mobile-responsive design
- Smooth animations

## 🔧 Technical Details

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Charts:** Plotly.js
- **Data Source:** CoinGecko API (with mock fallback)
- **Port:** 8080 (configurable in app.py)

## 🧪 Testing

Run the test script to verify everything works:
```bash
python3 test_app.py
```

## 📱 Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 🎯 Demo Data

When the CoinGecko API is rate limited, the app uses realistic mock data:
- Current price: ~$114,000
- Market cap: ~$2.3T
- 24h volume: ~$65B
- Historical data: 30 days of realistic price movements

## 🔄 Auto-refresh

The application automatically refreshes data every 30 seconds. You can also manually refresh using the refresh button or Ctrl+R.

## 📈 Chart Features

- Price line chart with volume bars
- Interactive hover information
- Responsive design
- Smooth animations
- Date range: 30 days

---

**Note:** This application is for educational and demonstration purposes. Always verify cryptocurrency data from multiple sources before making investment decisions. 