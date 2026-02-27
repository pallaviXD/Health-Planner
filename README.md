# 💪 AI-Powered Personalized Workout & Diet Planner for Students

A complete AI-powered web application that generates personalized workout and diet plans for students using machine learning and modern web technologies.

## 🌟 Features

### Core Functionality
- **AI-Powered Personalization**: Uses scikit-learn for ML-based profile analysis
- **BMI Calculation & Analysis**: Automatic health metrics calculation
- **7-Day Workout Plans**: Customized based on goals, BMI, and available time
- **Indian Diet Plans**: Culturally appropriate meals for students
- **Budget-Friendly**: Three budget levels (Low/Medium/High)
- **Downloadable Plans**: Export complete plan as formatted text file

### Personalization Factors
- Age, Gender, Height, Weight
- Fitness Goal (Fat Loss/Muscle Gain/Maintenance)
- Diet Preference (Vegetarian/Non-Vegetarian)
- Budget Level
- Available workout time per day

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **Streamlit** | Modern web UI framework |
| **scikit-learn** | Machine learning for personalization |
| **Hugging Face Transformers** | AI text generation capabilities |
| **pandas** | Data handling and processing |
| **NumPy** | Numerical computations |

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 2GB free disk space (for ML models)
- Internet connection (first-time setup)

## 🚀 Installation & Setup

### Step 1: Download the Project

```bash
# Clone or download the project files
cd workout-diet-planner
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** First installation may take 5-10 minutes as it downloads ML models and libraries.

### Step 4: Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## 📱 How to Use

### 1. Fill Your Profile (Sidebar)
- Enter personal details: age, gender, height, weight
- Select fitness goal
- Choose diet preference
- Set budget level
- Specify available workout time

### 2. Generate Plan
- Click "🚀 Generate My AI Plan" button
- Wait for AI analysis (2-3 seconds)

### 3. View Results
- **Metrics Dashboard**: BMI, intensity, focus area, AI score
- **7-Day Workout Plan**: Detailed daily exercises
- **Diet Plan**: Complete meal schedule with Indian foods
- **Health Tips**: AI-powered recommendations

### 4. Download
- Click download button to save complete plan as text file

## 🎯 Features Explained

### Machine Learning Personalization

The app uses **scikit-learn** to:
- Encode categorical inputs (gender, goal, diet, budget)
- Standardize numerical features (age, height, weight, time)
- Create personalized user profiles
- Calculate intensity scores based on multiple factors

### BMI-Based Adjustments
- **Underweight (< 18.5)**: Focus on strength building
- **Normal (18.5-25)**: Goal-specific training
- **Overweight (25-30)**: Moderate intensity cardio
- **Obese (> 30)**: Low-impact fat loss exercises

### Workout Plans

#### Fat Loss
- High cardio and HIIT sessions
- Circuit training
- Core strengthening
- 5-6 days active training

#### Muscle Gain
- Progressive overload strength training
- Split routines (chest/back/legs/shoulders)
- Compound movements
- Adequate rest days

#### Maintenance
- Balanced cardio and strength
- Full body workouts
- Flexibility training
- Sustainable routine

### Diet Plans

#### Vegetarian Options
- **Low Budget**: Dal, chapati, seasonal vegetables, peanuts
- **Medium Budget**: Paneer, tofu, quinoa, Greek yogurt, nuts

#### Non-Vegetarian Options
- **Low Budget**: Eggs, chicken, basic vegetables
- **Medium Budget**: Fish, lean meats, protein supplements

All plans include:
- 6-7 meals per day
- Calorie and protein targets
- Indian food preferences
- Student-friendly portions

## 📂 Project Structure

```
workout-diet-planner/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md             # Documentation (this file)
```

## 🔧 Troubleshooting

### Issue: Dependencies installation fails
**Solution:**
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install dependencies one by one
pip install streamlit
pip install scikit-learn
pip install pandas numpy
pip install transformers torch
```

### Issue: Streamlit won't start
**Solution:**
```bash
# Check if streamlit is installed
streamlit --version

# Try running on different port
streamlit run app.py --server.port 8502
```

### Issue: Module not found errors
**Solution:**
```bash
# Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Issue: App is slow on first run
**Explanation:** First run downloads ML models. Subsequent runs will be much faster.

## 💡 Usage Tips

### For Best Results
1. **Be Honest**: Provide accurate measurements
2. **Start Slow**: Begin with lower intensity if you're a beginner
3. **Stay Consistent**: Follow the plan for at least 4 weeks
4. **Track Progress**: Weigh yourself weekly, same time
5. **Adjust Portions**: Listen to your body's hunger signals
6. **Stay Hydrated**: Drink water throughout the day

### Workout Tips
- Always warm up (5-10 minutes)
- Focus on form over weight
- Progressive overload gradually
- Rest when body needs it
- Cool down and stretch

### Diet Tips
- Meal prep on weekends
- Buy seasonal vegetables (cheaper)
- Cook in bulk to save time
- Stay consistent with meal timing
- Don't skip breakfast

## 🎓 Perfect for Students

### Why This App?
- ✅ **No Gym Required**: Bodyweight exercises included
- ✅ **Budget-Friendly**: Affordable meal options
- ✅ **Time-Efficient**: 15-120 min workout options
- ✅ **Indian Foods**: Familiar, accessible ingredients
- ✅ **Free to Use**: No subscriptions or hidden costs
- ✅ **Offline Capable**: Runs locally on your machine

### Student Benefits
- Save money on gym trainers
- No expensive meal plans
- Flexible workout schedules
- Cultural food preferences
- Privacy (data stays local)

## 🔒 Privacy & Security

- ✅ All data processed locally
- ✅ No data sent to external servers
- ✅ No account creation required
- ✅ No tracking or analytics
- ✅ Complete privacy

## 📚 References

### Technologies Used
- [Python](https://www.python.org/) - Programming language
- [Streamlit](https://streamlit.io/) - Web framework
- [scikit-learn](https://scikit-learn.org/) - Machine learning
- [Hugging Face](https://huggingface.co/) - AI models

### Learning Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Tutorials](https://scikit-learn.org/stable/tutorial/index.html)
- [Python for Data Science](https://www.python.org/about/gettingstarted/)

## ⚠️ Disclaimer

This application provides general fitness guidance based on common fitness principles and AI analysis. It is NOT a substitute for professional medical advice, diagnosis, or treatment.

**Important:**
- Consult a doctor before starting any new exercise program
- Seek professional advice if you have health conditions
- Stop exercising if you experience pain or discomfort
- Adjust diet plans based on allergies and preferences
- Results may vary based on individual factors

## 🤝 Contributing

This is an educational project. Feel free to:
- Fork and modify
- Add new features
- Improve algorithms
- Share with others

## 📝 License

This project is open source and available for educational purposes.

## 🎯 Future Enhancements

Potential features for future versions:
- Progress tracking dashboard
- Meal calorie calculator
- Exercise video demonstrations
- Social sharing features
- Mobile app version
- Multi-language support

## 💬 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the documentation
3. Verify all dependencies are installed

## 🌟 Acknowledgments

Built with ❤️ for students who want to stay fit without breaking the bank.

Special thanks to:
- Streamlit team for the amazing framework
- scikit-learn contributors
- Hugging Face community
- Open source community

---

**Made for Students, By Students** 💪🎓

*Stay Fit, Stay Healthy, Stay Focused!*

---

## 📊 Technical Details

### ML Pipeline
1. **Data Collection**: User inputs via Streamlit form
2. **Preprocessing**: Label encoding + standardization
3. **Feature Engineering**: Create user profile vector
4. **Analysis**: Calculate intensity scores
5. **Generation**: Create personalized plans
6. **Output**: Display + download options

### Performance
- **Load Time**: 2-3 seconds (after initial setup)
- **Generation Time**: < 1 second
- **Memory Usage**: ~500MB (with ML models)
- **Disk Space**: ~2GB (including dependencies)

### Compatibility
- **OS**: Windows, macOS, Linux
- **Python**: 3.8, 3.9, 3.10, 3.11
- **Browsers**: Chrome, Firefox, Safari, Edge

---

**Version**: 1.0.0  
**Last Updated**: 2025  
**Status**: Production Ready ✅
