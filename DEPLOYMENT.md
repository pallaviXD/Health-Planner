# 🚀 Deployment Guide

## Deploy to Streamlit Cloud (FREE)

### Prerequisites
- GitHub account
- Your code pushed to GitHub repository

### Step-by-Step Deployment

#### 1. Go to Streamlit Cloud
Visit: https://share.streamlit.io/

#### 2. Sign In
- Click "Sign in" 
- Use your GitHub account

#### 3. Deploy New App
- Click "New app" button
- Select your repository
- Choose branch: `main` or `master`
- Main file path: `app.py`
- Click "Deploy!"

#### 4. Wait for Deployment
- First deployment takes 5-10 minutes
- Streamlit will install all dependencies from `requirements.txt`
- You'll get a public URL like: `https://your-app-name.streamlit.app`

### Configuration Files

The following files are already created for deployment:

- ✅ `requirements.txt` - Python dependencies
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `.gitignore` - Files to exclude from git
- ✅ `packages.txt` - System packages (if needed)
- ✅ `runtime.txt` - Python version

### Deployment Settings

**Recommended Settings:**
- Python version: 3.11
- Main file: `app.py`
- Branch: `main`

### After Deployment

Your app will be live at:
```
https://[your-app-name].streamlit.app
```

You can:
- ✅ Share the URL with anyone
- ✅ Update by pushing to GitHub (auto-deploys)
- ✅ View logs in Streamlit Cloud dashboard
- ✅ Manage settings and resources

### Troubleshooting

**Issue: Deployment fails**
- Check requirements.txt has correct versions
- Verify all files are pushed to GitHub
- Check Streamlit Cloud logs for errors

**Issue: App is slow**
- First load downloads ML models (normal)
- Subsequent loads are faster
- Consider using lighter models if needed

**Issue: Out of resources**
- Streamlit Cloud free tier has limits
- Optimize code if needed
- Consider upgrading plan for heavy usage

### Alternative Deployment Options

#### 1. Heroku
```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

#### 2. Railway
- Connect GitHub repository
- Railway auto-detects Streamlit
- Deploy with one click

#### 3. Render
- Connect GitHub repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `streamlit run app.py`

#### 4. AWS/GCP/Azure
- Use Docker container
- Deploy to cloud VM
- Configure reverse proxy

### Cost Comparison

| Platform | Free Tier | Paid Plans |
|----------|-----------|------------|
| Streamlit Cloud | ✅ Yes (1 app) | $20/month |
| Heroku | ❌ No | $7/month |
| Railway | ✅ Yes (limited) | $5/month |
| Render | ✅ Yes (limited) | $7/month |

### Best Practices

1. **Keep requirements.txt minimal**
   - Only include necessary packages
   - Specify version ranges

2. **Optimize app performance**
   - Use @st.cache_resource for models
   - Minimize data processing

3. **Monitor usage**
   - Check Streamlit Cloud analytics
   - Monitor resource usage

4. **Security**
   - Don't commit API keys
   - Use Streamlit secrets for sensitive data
   - Keep dependencies updated

### Support

- Streamlit Docs: https://docs.streamlit.io/
- Community Forum: https://discuss.streamlit.io/
- GitHub Issues: Report bugs in your repo

---

**Your app is ready to deploy! 🚀**

Just follow the steps above and your AI Fitness Planner will be live on the internet!
