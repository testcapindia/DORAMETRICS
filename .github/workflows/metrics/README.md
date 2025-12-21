# DORA Metrics Sample Repository

A complete example of automated DORA metrics tracking with **3 months of realistic data**.

## 📊 Current Performance (Sept-Dec 2024)

- **Deployment Frequency:** 0.97 per day (High 🥈)
- **Lead Time:** ~21 hours (Elite 🏆)
- **Failure Rate:** ~1.15% (Elite 🏆)
- **MTTR:** ~3.6 hours (High 🥈)

## 🎯 What's Included

- ✅ 87 deployments over 3 months
- ✅ 12 production incidents tracked
- ✅ 1 failed deployment
- ✅ Automated GitHub Actions workflow
- ✅ Python analysis script
- ✅ Ready-to-use CSV data

## 🚀 Quick Start

### View the Data
```bash
# Clone this repo
git clone https://github.com/YOUR-USERNAME/dora-metrics-sample.git
cd dora-metrics-sample

# View raw data
cat metrics/dora-data.csv

# Run analysis
python metrics/analyze.py
```

### Import to Google Sheets

1. Go to Google Sheets
2. File → Import
3. Upload `metrics/dora-data.csv`
4. Create charts and pivot tables

### Trigger a Test Deployment

1. Go to Actions tab
2. Click "DORA Metrics Tracker"
3. Click "Run workflow"
4. Watch it add a new entry to the CSV

## 📈 Monthly Trends

**September 2024:** 22 deployments, 3 incidents
**October 2024:** 27 deployments, 3 incidents  
**November 2024:** 25 deployments, 4 incidents
**December 2024:** 13 deployments, 2 incidents

## 🎓 How to Use This

1. **Explore the data** - See what 3 months of metrics looks like
2. **Run the analysis** - Use the Python script
3. **Fork this repo** - Make it your own
4. **Adapt the workflows** - Copy to your real projects

## 📚 Learn More

- DORA State of DevOps Report
- GitHub Actions Documentation

## 💡 Next Steps

Want to implement this in your organization? Check out the detailed setup guide in `SETUP.md`.
