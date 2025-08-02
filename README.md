# Bitcoin Price Tracker

A real-time Bitcoin price tracking application similar to CoinMarketCap, built with Flask and modern web technologies.

## Features

- **Real-time Bitcoin Price**: Live price updates every 30 seconds
- **Interactive Charts**: 30-day price and volume charts using Plotly
- **Market Statistics**: Market cap, volume, supply, and historical data
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Auto-refresh**: Automatic data updates with manual refresh option
- **Modern UI**: Beautiful gradient design with smooth animations
- **API Endpoints**: RESTful API for Bitcoin data

## Screenshots

The application features:
- Live Bitcoin price display with 24h change
- Interactive price charts with volume data
- Market statistics and supply information
- Real-time updates section
- Responsive design for all devices

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
bitcoin-price-tracker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── css/
    │   └── style.css     # Custom CSS styles
    └── js/
        └── app.js        # JavaScript functionality
```

## Features in Detail

### Real-time Price Tracking
- Fetches live Bitcoin data from CoinGecko API
- Updates every 30 seconds automatically
- Manual refresh button with loading states
- Price change indicators (green for positive, red for negative)

### Interactive Charts
- 30-day price history with volume data
- Responsive chart that adapts to screen size
- Hover tooltips with detailed information
- Smooth animations and transitions

### Market Statistics
- Current market cap and 24h volume
- Circulating supply vs maximum supply
- All-time high and low prices
- Formatted numbers with proper abbreviations (T, B, M, K)

### Responsive Design
- Mobile-first approach
- Bootstrap 5 framework
- Custom CSS with gradients and animations
- Touch-friendly interface

### API Endpoints
- `/api/bitcoin` - Get current Bitcoin data
- `/api/historical` - Get historical price data

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Charts**: Plotly.js
- **Styling**: Bootstrap 5, Font Awesome
- **Data Source**: CoinGecko API
- **Real-time Updates**: AJAX with Fetch API

## API Data Sources

The application uses the CoinGecko API to fetch:
- Current Bitcoin price and market data
- 24-hour price change percentage
- Market capitalization and trading volume
- Circulating supply and maximum supply
- All-time high and low prices
- Historical price data for charts

## Customization

### Changing Update Interval
Edit the `updateInterval` property in `static/js/app.js`:
```javascript
this.updateInterval = 30000; // 30 seconds
```

### Modifying Chart Period
Edit the `days` parameter in `app.py`:
```python
params = {
    'vs_currency': 'usd',
    'days': '30',  # Change to '7', '14', '90', etc.
    'interval': 'daily'
}
```

### Adding More Cryptocurrencies
To track additional cryptocurrencies, modify the API calls in `app.py` to include other coin IDs from CoinGecko.

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Performance

- Lightweight and fast loading
- Optimized API calls with caching
- Efficient DOM updates
- Responsive chart rendering

## Security

- No sensitive data stored
- Uses public APIs only
- HTTPS recommended for production
- Input validation and error handling

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Install gunicorn: `pip install gunicorn`
2. Run with: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`
3. Set up reverse proxy (nginx/Apache)
4. Configure SSL certificate

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
1. Check the browser console for errors
2. Verify internet connection for API calls
3. Ensure all dependencies are installed
4. Check if CoinGecko API is accessible

## Future Enhancements

- Add more cryptocurrencies
- Implement price alerts
- Add portfolio tracking
- Include news feed
- Add price predictions
- Implement user accounts
- Add mobile app version

---

**Note**: This application is for educational and informational purposes. Always verify cryptocurrency data from multiple sources before making investment decisions. 