#!/usr/bin/env python3
"""
Test script for Bitcoin Price Tracker
"""

import requests
import json
from datetime import datetime

def test_api_endpoints():
    """Test all API endpoints"""
    base_url = "http://localhost:8080"
    
    print("🧪 Testing Bitcoin Price Tracker API...")
    print("=" * 50)
    
    # Test main page
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Main page: OK")
        else:
            print(f"❌ Main page: Failed (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Main page: Error - {e}")
    
    # Test Bitcoin API
    try:
        response = requests.get(f"{base_url}/api/bitcoin")
        if response.status_code == 200:
            data = response.json()
            print("✅ Bitcoin API: OK")
            print(f"   Current Price: ${data['price_usd']:,.2f}")
            print(f"   24h Change: {data['price_change_24h']:.2f}%")
            print(f"   Market Cap: ${data['market_cap']:,.0f}")
        else:
            print(f"❌ Bitcoin API: Failed (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Bitcoin API: Error - {e}")
    
    # Test Historical API
    try:
        response = requests.get(f"{base_url}/api/historical")
        if response.status_code == 200:
            data = response.json()
            print("✅ Historical API: OK")
            print(f"   Data Points: {len(data['dates'])}")
            print(f"   Date Range: {data['dates'][0]} to {data['dates'][-1]}")
        else:
            print(f"❌ Historical API: Failed (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Historical API: Error - {e}")
    
    print("=" * 50)
    print("🎉 All tests completed!")

if __name__ == "__main__":
    test_api_endpoints() 