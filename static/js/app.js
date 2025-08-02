// Bitcoin Price Tracker JavaScript

class BitcoinTracker {
    constructor() {
        this.updateInterval = 30000; // 30 seconds
        this.lastPrice = 0;
        this.init();
    }

    init() {
        this.loadInitialData();
        this.startAutoUpdate();
        this.setupEventListeners();
    }

    async loadInitialData() {
        try {
            const response = await fetch('/api/bitcoin');
            const data = await response.json();
            
            if (data.error) {
                console.error('Error loading Bitcoin data:', data.error);
                return;
            }
            
            this.updateUI(data);
            this.updateLastUpdated();
        } catch (error) {
            console.error('Failed to load Bitcoin data:', error);
        }
    }

    async refreshData() {
        const refreshBtn = document.querySelector('button[onclick="refreshData()"]');
        if (refreshBtn) {
            refreshBtn.disabled = true;
            refreshBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Refreshing...';
        }

        try {
            const response = await fetch('/api/bitcoin');
            const data = await response.json();
            
            if (data.error) {
                console.error('Error refreshing Bitcoin data:', data.error);
                return;
            }
            
            this.updateUI(data);
            this.updateLastUpdated();
            
            // Show success message
            this.showNotification('Data refreshed successfully!', 'success');
        } catch (error) {
            console.error('Failed to refresh Bitcoin data:', error);
            this.showNotification('Failed to refresh data. Please try again.', 'error');
        } finally {
            if (refreshBtn) {
                refreshBtn.disabled = false;
                refreshBtn.innerHTML = '<i class="fas fa-sync-alt"></i> Refresh';
            }
        }
    }

    updateUI(data) {
        // Format numbers
        const price = this.formatCurrency(data.price_usd);
        const marketCap = this.formatLargeNumber(data.market_cap);
        const volume = this.formatLargeNumber(data.volume_24h);
        const change = data.price_change_24h;
        const circulatingSupply = this.formatNumber(data.circulating_supply);
        const ath = this.formatCurrency(data.ath);
        const atl = this.formatCurrency(data.atl);

        // Update main price display
        this.updateElement('current-price', price);
        this.updateElement('update-price', price);

        // Update price change
        const changeElement = document.getElementById('price-change');
        if (changeElement) {
            const changeAmount = changeElement.querySelector('.change-amount');
            const changePeriod = changeElement.querySelector('.change-period');
            
            if (changeAmount) {
                changeAmount.textContent = `${change.toFixed(2)}%`;
                changeAmount.className = `change-amount ${change >= 0 ? 'positive' : 'negative'}`;
            }
            
            if (changePeriod) {
                changePeriod.textContent = '(24h)';
            }
        }

        // Update 24h change in real-time section
        this.updateElement('update-change', `${change.toFixed(2)}%`);

        // Update market statistics
        this.updateElement('market-cap', marketCap);
        this.updateElement('volume-24h', volume);
        this.updateElement('update-market-cap', marketCap);
        this.updateElement('update-volume', volume);

        // Update supply and historical data
        this.updateElement('circulating-supply', `${circulatingSupply} BTC`);
        this.updateElement('ath', ath);
        this.updateElement('atl', atl);

        // Add price update animation
        this.addPriceUpdateAnimation();
    }

    updateElement(id, value) {
        const element = document.getElementById(id);
        if (element) {
            // Check if value has changed for animation
            if (element.textContent !== value) {
                element.classList.add('price-update');
                setTimeout(() => {
                    element.classList.remove('price-update');
                }, 500);
            }
            element.textContent = value;
        }
    }

    formatCurrency(amount) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        }).format(amount);
    }

    formatLargeNumber(num) {
        if (num >= 1e12) {
            return `$${(num / 1e12).toFixed(2)}T`;
        } else if (num >= 1e9) {
            return `$${(num / 1e9).toFixed(2)}B`;
        } else if (num >= 1e6) {
            return `$${(num / 1e6).toFixed(2)}M`;
        } else if (num >= 1e3) {
            return `$${(num / 1e3).toFixed(2)}K`;
        } else {
            return `$${num.toFixed(2)}`;
        }
    }

    formatNumber(num) {
        return new Intl.NumberFormat('en-US').format(num);
    }

    updateLastUpdated() {
        const now = new Date();
        const timeString = now.toLocaleTimeString();
        const element = document.getElementById('last-updated');
        if (element) {
            element.textContent = `Last updated: ${timeString}`;
        }
    }

    addPriceUpdateAnimation() {
        const priceElements = document.querySelectorAll('#current-price, #update-price');
        priceElements.forEach(element => {
            element.classList.add('price-update');
            setTimeout(() => {
                element.classList.remove('price-update');
            }, 500);
        });
    }

    startAutoUpdate() {
        setInterval(() => {
            this.refreshData();
        }, this.updateInterval);
    }

    setupEventListeners() {
        // Add keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'r') {
                e.preventDefault();
                this.refreshData();
            }
        });

        // Add click handlers for interactive elements
        document.addEventListener('click', (e) => {
            if (e.target.closest('.stat-card')) {
                this.showTooltip(e.target.closest('.stat-card'));
            }
        });
    }

    showTooltip(element) {
        // Create tooltip for statistics
        const tooltip = document.createElement('div');
        tooltip.className = 'tooltip';
        tooltip.textContent = 'Click to see more details';
        tooltip.style.cssText = `
            position: absolute;
            background: #333;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 12px;
            z-index: 1000;
            pointer-events: none;
        `;
        
        document.body.appendChild(tooltip);
        
        const rect = element.getBoundingClientRect();
        tooltip.style.left = rect.left + 'px';
        tooltip.style.top = (rect.top - 30) + 'px';
        
        setTimeout(() => {
            document.body.removeChild(tooltip);
        }, 2000);
    }

    showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#28a745' : type === 'error' ? '#dc3545' : '#17a2b8'};
            color: white;
            padding: 15px 20px;
            border-radius: 5px;
            z-index: 1000;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            animation: slideIn 0.3s ease-out;
        `;
        
        document.body.appendChild(notification);
        
        // Remove notification after 3 seconds
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease-in';
            setTimeout(() => {
                if (document.body.contains(notification)) {
                    document.body.removeChild(notification);
                }
            }, 300);
        }, 3000);
    }
}

// Initialize the tracker when the page loads
document.addEventListener('DOMContentLoaded', () => {
    window.bitcoinTracker = new BitcoinTracker();
});

// Global refresh function
function refreshData() {
    if (window.bitcoinTracker) {
        window.bitcoinTracker.refreshData();
    }
}

// Add CSS animations for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Add chart interaction handlers
document.addEventListener('DOMContentLoaded', () => {
    const chartElement = document.getElementById('price-chart');
    if (chartElement) {
        // Add chart interaction handlers
        chartElement.addEventListener('click', (e) => {
            // Handle chart interactions
            console.log('Chart clicked:', e);
        });
    }
});

// Add responsive chart resizing
window.addEventListener('resize', () => {
    const chartElement = document.getElementById('price-chart');
    if (chartElement && window.Plotly) {
        Plotly.Plots.resize(chartElement);
    }
}); 