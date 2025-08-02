#!/bin/bash

echo "🚀 Starting Jayden's BTC Price Tracker..."
echo "🌐 Access at: http://localhost:8080"
echo "📡 Network access: http://192.168.1.105:8080"
echo "⛔ Press Ctrl+C to stop the server"
echo ""

# Move to script directory
cd "$(dirname "$0")"

# Start the Flask app
python3 app.py
app.run(host='0.0.0.0', port=8080)
