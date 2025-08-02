# 🚀 Deploy Jayden's Bitcoin Price Tracker

## Quick Deploy Options

### Option 1: Railway (Recommended - Free)
1. **Sign up at:** https://railway.app
2. **Connect your GitHub** (upload your code first)
3. **Deploy automatically** - Railway detects Flask apps

### Option 2: Render (Free)
1. **Sign up at:** https://render.com
2. **Create new Web Service**
3. **Connect your repository**
4. **Set build command:** `pip install -r requirements.txt`
5. **Set start command:** `gunicorn app:app`

### Option 3: Heroku (Free tier ended, but cheap)
1. **Install Heroku CLI**
2. **Create Procfile:**
   ```
   web: gunicorn app:app
   ```
3. **Deploy:**
   ```bash
   heroku create jaydens-bitcoin-tracker
   git push heroku main
   ```

## 📁 Files Needed for Deployment

Make sure you have:
- ✅ `app.py` (main Flask app)
- ✅ `requirements.txt` (dependencies)
- ✅ `templates/` folder
- ✅ `static/` folder
- ✅ `README.md`

## 🔧 Quick Setup for Cloud Deployment

### 1. Create a Procfile (for Heroku/Railway)
```bash
echo "web: gunicorn app:app" > Procfile
```

### 2. Update requirements.txt (if needed)
```bash
pip freeze > requirements.txt
```

### 3. Test locally first
```bash
gunicorn app:app
```

## 🌐 After Deployment

Your app will be available at:
- **Railway:** `https://your-app-name.railway.app`
- **Render:** `https://your-app-name.onrender.com`
- **Heroku:** `https://your-app-name.herokuapp.com`

## 📱 Share Your App

Once deployed, you can share:
- **The URL** with anyone worldwide
- **QR code** for mobile access
- **Embed** in other websites

## 🔄 Keep It Running

Cloud platforms will:
- ✅ Keep your app running 24/7
- ✅ Auto-restart if it crashes
- ✅ Handle traffic automatically
- ✅ Provide HTTPS security

---

**Pro Tip:** Railway and Render are the easiest for beginners and have generous free tiers! 