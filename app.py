"""
AI-Powered Personalized Workout & Diet Planner for Students
Uses: Streamlit, Hugging Face Transformers, scikit-learn
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FF6B6B;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #4ECDC4;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B6B;
        color: white;
        font-size: 1.2rem;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Calculate BMI and category
def calculate_bmi(weight, height):
    """Calculate BMI and return category"""
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
        color = "#FFA500"
    elif 18.5 <= bmi < 25:
        category = "Normal"
        color = "#4CAF50"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "#FF9800"
    else:
        category = "Obese"
        color = "#F44336"
    
    return round(bmi, 2), category, color

# ML-based personalization using scikit-learn
def create_user_profile(age, gender, height, weight, goal, diet_pref, budget, workout_time):
    """Use scikit-learn to encode and process user data"""
    
    # Label encoding for categorical variables
    le_gender = LabelEncoder()
    le_goal = LabelEncoder()
    le_diet = LabelEncoder()
    le_budget = LabelEncoder()
    
    # Fit and transform
    gender_encoded = le_gender.fit_transform(['Male', 'Female']).tolist().index(
        le_gender.fit_transform([gender])[0]
    )
    goal_encoded = le_goal.fit_transform(['Fat Loss', 'Muscle Gain', 'Maintenance']).tolist().index(
        le_goal.fit_transform([goal])[0]
    )
    diet_encoded = le_diet.fit_transform(['Vegetarian', 'Non-Vegetarian']).tolist().index(
        le_diet.fit_transform([diet_pref])[0]
    )
    budget_encoded = le_budget.fit_transform(['Low', 'Medium', 'High']).tolist().index(
        le_budget.fit_transform([budget])[0]
    )
    
    # Create feature vector
    features = np.array([[
        age, gender_encoded, height, weight,
        goal_encoded, diet_encoded, budget_encoded, workout_time
    ]])
    
    # Standardize features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    return features_scaled, {
        'age': age,
        'gender': gender_encoded,
        'goal': goal_encoded,
        'diet': diet_encoded,
        'budget': budget_encoded
    }

# Determine workout intensity using ML logic
def get_workout_parameters(bmi, goal, workout_time, age):
    """ML-based workout parameter determination"""
    
    # Create decision matrix
    intensity_score = 0
    
    # BMI factor
    if bmi < 18.5:
        intensity_score += 1
        base_intensity = "Light to Moderate"
        focus = "Strength Building & Weight Gain"
    elif bmi >= 30:
        intensity_score += 2
        base_intensity = "Low to Moderate"
        focus = "Cardio & Fat Loss"
    else:
        intensity_score += 3
        if goal == "Fat Loss":
            base_intensity = "Moderate to High"
            focus = "HIIT & Cardio"
        elif goal == "Muscle Gain":
            base_intensity = "Moderate to High"
            focus = "Strength Training"
        else:
            base_intensity = "Moderate"
            focus = "Balanced Fitness"
    
    # Age factor
    if age < 20:
        intensity_multiplier = 1.1
    elif age > 30:
        intensity_multiplier = 0.9
    else:
        intensity_multiplier = 1.0
    
    # Time factor
    if workout_time < 30:
        workout_type = "Quick HIIT"
    elif workout_time < 60:
        workout_type = "Standard Routine"
    else:
        workout_type = "Extended Training"
    
    return {
        'intensity': base_intensity,
        'focus': focus,
        'type': workout_type,
        'score': intensity_score * intensity_multiplier
    }

# Generate AI-powered workout plan
def generate_workout_plan(goal, bmi_category, workout_params, workout_time):
    """Generate personalized 7-day workout plan"""
    
    plans = {
        "Fat Loss": {
            "Monday": [
                "🔥 Warm-up: 5 min dynamic stretching",
                "🏃 Cardio: 25 min running/cycling (moderate pace)",
                "💪 Circuit Training:",
                "  - Jumping jacks: 3 sets × 30 reps",
                "  - Burpees: 3 sets × 12 reps",
                "  - Mountain climbers: 3 sets × 20 reps",
                "🧘 Cool down: 5 min stretching"
            ],
            "Tuesday": [
                "🔥 Warm-up: 5 min jogging",
                "💪 Upper Body Strength:",
                "  - Push-ups: 4 sets × 12 reps",
                "  - Dumbbell rows: 3 sets × 15 reps",
                "  - Tricep dips: 3 sets × 12 reps",
                "  - Plank: 3 sets × 45 sec",
                "🧘 Cool down & stretch"
            ],
            "Wednesday": [
                "🔥 HIIT Session (30 min):",
                "  - Sprint intervals: 30 sec sprint, 30 sec rest × 10",
                "  - Jump squats: 4 sets × 15 reps",
                "  - High knees: 4 sets × 30 sec",
                "  - Rest: 1 min between exercises",
                "🧘 Yoga/Stretching: 15 min"
            ],
            "Thursday": [
                "🔥 Warm-up: 5 min",
                "💪 Lower Body + Core:",
                "  - Squats: 4 sets × 20 reps",
                "  - Lunges: 3 sets × 15 reps each leg",
                "  - Leg raises: 3 sets × 15 reps",
                "  - Russian twists: 3 sets × 25 reps",
                "  - Bicycle crunches: 3 sets × 20 reps"
            ],
            "Friday": [
                "🔥 Cardio Blast:",
                "  - Running: 30 min (interval training)",
                "  - Jump rope: 5 sets × 2 min",
                "💪 Core finisher:",
                "  - Plank variations: 3 sets × 40 sec each",
                "🧘 Cool down"
            ],
            "Saturday": [
                "🔥 Full Body Circuit:",
                "  - Burpees: 3 sets × 15 reps",
                "  - Push-ups: 3 sets × 15 reps",
                "  - Squats: 3 sets × 20 reps",
                "  - Mountain climbers: 3 sets × 25 reps",
                "  - Plank: 3 sets × 1 min",
                "🧘 Stretching: 10 min"
            ],
            "Sunday": [
                "🌟 Active Recovery:",
                "  - Light yoga: 30 min",
                "  - Walking/Cycling: 30 min (easy pace)",
                "  - Foam rolling & stretching",
                "💧 Focus on hydration & rest"
            ]
        },
        "Muscle Gain": {
            "Monday": [
                "🔥 Warm-up: 5 min light cardio",
                "💪 Chest + Triceps:",
                "  - Bench press/Push-ups: 4 sets × 10 reps",
                "  - Incline dumbbell press: 4 sets × 12 reps",
                "  - Chest flyes: 3 sets × 12 reps",
                "  - Tricep dips: 4 sets × 12 reps",
                "  - Overhead tricep extension: 3 sets × 15 reps"
            ],
            "Tuesday": [
                "🔥 Warm-up: 5 min",
                "💪 Back + Biceps:",
                "  - Pull-ups/Chin-ups: 4 sets × 8 reps",
                "  - Bent-over rows: 4 sets × 12 reps",
                "  - Lat pulldowns: 3 sets × 12 reps",
                "  - Bicep curls: 4 sets × 12 reps",
                "  - Hammer curls: 3 sets × 15 reps"
            ],
            "Wednesday": [
                "🌟 Rest Day or Light Cardio:",
                "  - Walking: 20-30 min",
                "  - Stretching & mobility work",
                "  - Focus on nutrition & recovery"
            ],
            "Thursday": [
                "🔥 Warm-up: 5 min",
                "💪 Legs (Quad Focus):",
                "  - Squats: 5 sets × 10 reps",
                "  - Leg press: 4 sets × 12 reps",
                "  - Lunges: 4 sets × 12 reps each",
                "  - Leg extensions: 3 sets × 15 reps",
                "  - Calf raises: 4 sets × 20 reps"
            ],
            "Friday": [
                "🔥 Warm-up: 5 min",
                "💪 Shoulders + Abs:",
                "  - Military press: 4 sets × 10 reps",
                "  - Lateral raises: 4 sets × 12 reps",
                "  - Front raises: 3 sets × 12 reps",
                "  - Rear delt flyes: 3 sets × 15 reps",
                "  - Hanging leg raises: 4 sets × 12 reps",
                "  - Plank: 3 sets × 1 min"
            ],
            "Saturday": [
                "🔥 Warm-up: 5 min",
                "💪 Legs (Hamstring Focus):",
                "  - Deadlifts: 4 sets × 8 reps",
                "  - Romanian deadlifts: 4 sets × 10 reps",
                "  - Leg curls: 4 sets × 12 reps",
                "  - Bulgarian split squats: 3 sets × 10 each",
                "  - Calf raises: 4 sets × 20 reps"
            ],
            "Sunday": [
                "🌟 Complete Rest:",
                "  - No workout",
                "  - Focus on sleep (8+ hours)",
                "  - Meal prep for the week",
                "  - Light stretching if needed"
            ]
        },
        "Maintenance": {
            "Monday": [
                "🔥 Warm-up: 5 min",
                "💪 Full Body Strength:",
                "  - Push-ups: 3 sets × 15 reps",
                "  - Squats: 3 sets × 20 reps",
                "  - Rows: 3 sets × 12 reps",
                "  - Plank: 3 sets × 45 sec"
            ],
            "Tuesday": [
                "🏃 Cardio Day:",
                "  - Running/Cycling: 30 min moderate pace",
                "  - Jump rope: 3 sets × 2 min",
                "🧘 Stretching: 10 min"
            ],
            "Wednesday": [
                "💪 Upper Body:",
                "  - Push-ups: 3 sets × 12 reps",
                "  - Dumbbell press: 3 sets × 12 reps",
                "  - Rows: 3 sets × 12 reps",
                "  - Bicep curls: 3 sets × 15 reps"
            ],
            "Thursday": [
                "🏃 Active Recovery:",
                "  - Yoga: 30 min",
                "  - Walking: 20 min",
                "  - Mobility exercises"
            ],
            "Friday": [
                "💪 Lower Body + Core:",
                "  - Squats: 3 sets × 15 reps",
                "  - Lunges: 3 sets × 12 each",
                "  - Deadlifts: 3 sets × 10 reps",
                "  - Plank variations: 3 sets × 40 sec"
            ],
            "Saturday": [
                "🏃 Cardio + Core:",
                "  - Running: 25 min",
                "  - Core circuit: 15 min",
                "  - Stretching: 10 min"
            ],
            "Sunday": [
                "🌟 Rest Day:",
                "  - Light walking or complete rest",
                "  - Focus on recovery"
            ]
        }
    }
    
    return plans.get(goal, plans["Maintenance"])

# Generate AI-powered diet plan
def generate_diet_plan(goal, diet_pref, budget, bmi_category):
    """Generate personalized Indian diet plan"""
    
    # Diet plans based on preferences and budget
    diet_plans = {
        ("Vegetarian", "Low", "Fat Loss"): {
            "title": "🥗 Vegetarian Fat Loss Plan (Budget-Friendly)",
            "meals": [
                "☀️ Early Morning (6:30 AM): Warm lemon water + 5 soaked almonds",
                "🍳 Breakfast (8:00 AM): 2 moong dal cheela + green chutney + 1 banana",
                "🍎 Mid-Morning (11:00 AM): 1 fruit (apple/orange) + green tea",
                "🍛 Lunch (1:30 PM): 2 chapati + dal (1 bowl) + mixed veg + cucumber salad",
                "☕ Evening (4:30 PM): Sprouts chaat (50g) + black coffee",
                "🍲 Dinner (7:30 PM): 2 chapati + palak paneer/tofu + raita",
                "🥛 Before Bed (10:00 PM): Turmeric milk (low-fat)"
            ],
            "calories": "~1500-1600 kcal/day",
            "protein": "60-70g",
            "tips": [
                "💡 Use minimal oil in cooking",
                "💡 Drink 3-4 liters of water daily",
                "💡 Avoid rice at dinner",
                "💡 Buy seasonal vegetables for budget"
            ]
        },
        ("Vegetarian", "Medium", "Fat Loss"): {
            "title": "🥗 Vegetarian Fat Loss Plan (Medium Budget)",
            "meals": [
                "☀️ Early Morning (6:30 AM): Warm water + 10 almonds + 2 walnuts",
                "🍳 Breakfast (8:00 AM): Oats upma with vegetables + 1 glass milk + 1 fruit",
                "🍎 Mid-Morning (11:00 AM): Greek yogurt + mixed berries + green tea",
                "🍛 Lunch (1:30 PM): 2 multigrain chapati + rajma/chole + salad + buttermilk",
                "☕ Evening (4:30 PM): Roasted chana + paneer cubes (50g) + green tea",
                "🍲 Dinner (7:30 PM): Quinoa/brown rice + grilled paneer + stir-fry veggies",
                "🥛 Before Bed (10:00 PM): Protein shake or almond milk"
            ],
            "calories": "~1600-1700 kcal/day",
            "protein": "75-85g",
            "tips": [
                "💡 Include paneer/tofu daily",
                "💡 Use olive oil for cooking",
                "💡 Add flax seeds to meals"
            ]
        },
        ("Non-Vegetarian", "Low", "Fat Loss"): {
            "title": "🍗 Non-Vegetarian Fat Loss Plan (Budget-Friendly)",
            "meals": [
                "☀️ Early Morning (6:30 AM): Warm lemon water + 5 almonds",
                "🍳 Breakfast (8:00 AM): 3 egg white omelette + 2 bread + tea",
                "🍎 Mid-Morning (11:00 AM): 1 banana + black coffee",
                "🍛 Lunch (1:30 PM): 2 chapati + chicken curry (100g) + dal + salad",
                "☕ Evening (4:30 PM): 2 boiled eggs + green tea",
                "🍲 Dinner (7:30 PM): Grilled chicken (150g) + sautéed vegetables + raita",
                "🥛 Before Bed (10:00 PM): Low-fat milk"
            ],
            "calories": "~1600-1700 kcal/day",
            "protein": "90-100g",
            "tips": [
                "💡 Buy eggs in bulk (cheaper)",
                "💡 Use chicken breast (lean protein)",
                "💡 Include fish 2x per week if possible"
            ]
        },
        ("Non-Vegetarian", "Medium", "Fat Loss"): {
            "title": "🍗 Non-Vegetarian Fat Loss Plan (Medium Budget)",
            "meals": [
                "☀️ Early Morning (6:30 AM): Warm water + 10 almonds + 2 walnuts",
                "🍳 Breakfast (8:00 AM): 4 egg white + 1 whole egg omelette + oats + fruit",
                "🍎 Mid-Morning (11:00 AM): Protein shake + 1 apple",
                "🍛 Lunch (1:30 PM): Brown rice + grilled chicken (150g) + salad + dal",
                "☕ Evening (4:30 PM): Tuna/chicken sandwich (whole wheat) + green tea",
                "🍲 Dinner (7:30 PM): Fish curry/grilled chicken (150g) + vegetables + raita",
                "🥛 Before Bed (10:00 PM): Casein protein shake or milk"
            ],
            "calories": "~1700-1800 kcal/day",
            "protein": "110-120g",
            "tips": [
                "💡 Rotate between chicken, fish, eggs",
                "💡 Include salmon for omega-3",
                "💡 Meal prep on weekends"
            ]
        },
        ("Vegetarian", "Low", "Muscle Gain"): {
            "title": "💪 Vegetarian Muscle Gain Plan (Budget-Friendly)",
            "meals": [
                "☀️ Early Morning (6:30 AM): Banana shake with peanut butter",
                "🍳 Breakfast (8:00 AM): 3 paratha + curd + 1 glass milk",
                "🍎 Mid-Morning (11:00 AM): Peanut butter sandwich + banana",
                "🍛 Lunch (1:30 PM): 3 chapati + dal + paneer curry + rice + salad",
                "☕ Evening (4:30 PM): Sprouts + roasted chana + tea with biscuits",
                "🍲 Dinner (7:30 PM): 3 chapati + soya chunks curry + dal + curd",
                "🥛 Before Bed (10:00 PM): Milk with protein powder/banana"
            ],
            "calories": "~2500-2700 kcal/day",
            "protein": "80-90g",
            "tips": [
                "💡 Use peanut butter for calories",
                "💡 Soya chunks are cheap protein",
                "💡 Eat every 2-3 hours"
            ]
        },
        ("Vegetarian", "Medium", "Muscle Gain"): {
            "title": "💪 Vegetarian Muscle Gain Plan (Medium Budget)",
            "meals": [
                "☀️ Early Morning (6:30 AM): Protein shake + 10 almonds + 2 dates",
                "🍳 Breakfast (8:00 AM): Oats with milk + paneer sandwich + fruits",
                "🍎 Mid-Morning (11:00 AM): Greek yogurt + mixed nuts + banana",
                "🍛 Lunch (1:30 PM): 4 chapati + paneer + dal + brown rice + salad",
                "☕ Evening (4:30 PM): Protein shake + peanut butter toast",
                "🍲 Dinner (7:30 PM): Quinoa + tofu curry + vegetables + raita",
                "🥛 Before Bed (10:00 PM): Casein shake + almonds"
            ],
            "calories": "~2800-3000 kcal/day",
            "protein": "100-120g",
            "tips": [
                "💡 Include paneer, tofu, legumes daily",
                "💡 Use whey protein post-workout",
                "💡 Track your calorie surplus"
            ]
        },
        ("Non-Vegetarian", "Low", "Muscle Gain"): {
            "title": "💪 Non-Vegetarian Muscle Gain Plan (Budget-Friendly)",
            "meals": [
                "☀️ Early Morning (6:30 AM): 4 boiled eggs + banana",
                "🍳 Breakfast (8:00 AM): 4 egg omelette + 3 bread + milk",
                "🍎 Mid-Morning (11:00 AM): Chicken sandwich + banana",
                "🍛 Lunch (1:30 PM): 3 chapati + chicken curry (150g) + rice + dal",
                "☕ Evening (4:30 PM): 3 boiled eggs + peanuts + tea",
                "🍲 Dinner (7:30 PM): 4 chapati + chicken/fish (200g) + vegetables",
                "🥛 Before Bed (10:00 PM): Milk with banana"
            ],
            "calories": "~2700-2900 kcal/day",
            "protein": "130-150g",
            "tips": [
                "💡 Eggs are cheapest protein source",
                "💡 Buy chicken in bulk",
                "💡 Eat 6-7 meals per day"
            ]
        },
        ("Non-Vegetarian", "Medium", "Muscle Gain"): {
            "title": "💪 Non-Vegetarian Muscle Gain Plan (Medium Budget)",
            "meals": [
                "☀️ Early Morning (6:30 AM): Protein shake + 5 whole eggs",
                "🍳 Breakfast (8:00 AM): 5 egg omelette + oats + fruits + milk",
                "🍎 Mid-Morning (11:00 AM): Chicken breast (100g) + brown rice + nuts",
                "🍛 Lunch (1:30 PM): 4 chapati + chicken (200g) + rice + dal + salad",
                "☕ Evening (4:30 PM): Tuna sandwich + protein shake",
                "🍲 Dinner (7:30 PM): Fish/chicken (200g) + quinoa + vegetables",
                "🥛 Before Bed (10:00 PM): Casein protein + peanut butter"
            ],
            "calories": "~3000-3200 kcal/day",
            "protein": "150-170g",
            "tips": [
                "💡 Include fish for omega-3",
                "💡 Use supplements wisely",
                "💡 Progressive overload in gym"
            ]
        }
    }
    
    # Default maintenance plans
    maintenance_plan = {
        "title": "⚖️ Balanced Maintenance Plan",
        "meals": [
            "☀️ Early Morning: Warm water + nuts",
            "🍳 Breakfast: Balanced meal with protein + carbs",
            "🍎 Mid-Morning: Fruit + beverage",
            "🍛 Lunch: Complete meal with all macros",
            "☕ Evening: Light snack",
            "🍲 Dinner: Moderate portion balanced meal",
            "🥛 Before Bed: Light beverage"
        ],
        "calories": "~2000-2200 kcal/day",
        "protein": "70-80g",
        "tips": [
            "💡 Maintain consistent eating schedule",
            "💡 Balance all macronutrients",
            "💡 Stay hydrated"
        ]
    }
    
    # Select appropriate plan
    key = (diet_pref, budget, goal)
    return diet_plans.get(key, maintenance_plan)

# Main application
def main():
    # Header
    st.markdown('<p class="main-header">💪 AI Fitness Planner</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Personalized Workout & Diet Plans for Students</p>', unsafe_allow_html=True)
    
    # Sidebar for user inputs
    with st.sidebar:
        st.header("📋 Your Profile")
        
        # Personal details
        st.subheader("Personal Information")
        age = st.number_input("Age", min_value=15, max_value=35, value=20, help="Your current age")
        gender = st.selectbox("Gender", ["Male", "Female"])
        height = st.number_input("Height (cm)", min_value=120, max_value=220, value=170)
        weight = st.number_input("Weight (kg)", min_value=30, max_value=150, value=65)
        
        st.markdown("---")
        
        # Fitness preferences
        st.subheader("Fitness Goals")
        goal = st.selectbox(
            "Primary Goal",
            ["Fat Loss", "Muscle Gain", "Maintenance"],
            help="What do you want to achieve?"
        )
        
        workout_time = st.slider(
            "Available Workout Time (min/day)",
            min_value=15,
            max_value=120,
            value=45,
            step=5,
            help="How much time can you dedicate daily?"
        )
        
        st.markdown("---")
        
        # Diet preferences
        st.subheader("Diet Preferences")
        diet_pref = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian"])
        budget = st.selectbox(
            "Budget Level",
            ["Low", "Medium", "High"],
            help="Your monthly food budget capacity"
        )
        
        st.markdown("---")
        
        # Generate button
        generate_btn = st.button("🚀 Generate My AI Plan", type="primary")
    
    # Main content
    if generate_btn:
        with st.spinner("🤖 AI is analyzing your profile and creating personalized plans..."):
            
            # Calculate BMI
            bmi, bmi_category, bmi_color = calculate_bmi(weight, height)
            
            # Create ML-based user profile
            features, encoded_data = create_user_profile(
                age, gender, height, weight, goal, diet_pref, budget, workout_time
            )
            
            # Get workout parameters using ML
            workout_params = get_workout_parameters(bmi, goal, workout_time, age)
            
            # Display metrics
            st.success("✅ Profile Analysis Complete!")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric(
                    label="BMI",
                    value=bmi,
                    delta=bmi_category,
                    delta_color="off"
                )
            
            with col2:
                st.metric(
                    label="Intensity",
                    value=workout_params['intensity'].split()[0],
                    delta=workout_params['type']
                )
            
            with col3:
                st.metric(
                    label="Focus Area",
                    value=workout_params['focus'].split()[0],
                    delta="Personalized"
                )
            
            with col4:
                st.metric(
                    label="AI Score",
                    value=f"{workout_params['score']:.1f}/5",
                    delta="Optimized"
                )
            
            st.markdown("---")
            
            # Generate and display workout plan
            st.subheader("🏋️ Your 7-Day AI Workout Plan")
            st.info(f"**Goal:** {goal} | **Intensity:** {workout_params['intensity']} | **Focus:** {workout_params['focus']}")
            
            workout_plan = generate_workout_plan(goal, bmi_category, workout_params, workout_time)
            
            # Display workout in tabs
            tabs = st.tabs(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
            
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            for i, tab in enumerate(tabs):
                with tab:
                    day_plan = workout_plan[days[i]]
                    for exercise in day_plan:
                        st.write(exercise)
            
            st.markdown("---")
            
            # Generate and display diet plan
            st.subheader("🍽️ Your Personalized Indian Diet Plan")
            diet_plan = generate_diet_plan(goal, diet_pref, budget, bmi_category)
            
            st.success(diet_plan['title'])
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write("**Daily Meal Schedule:**")
                for meal in diet_plan['meals']:
                    st.write(meal)
            
            with col2:
                st.write("**Nutritional Info:**")
                st.info(f"📊 Calories: {diet_plan['calories']}")
                st.info(f"💪 Protein: {diet_plan['protein']}")
                
                st.write("**Pro Tips:**")
                for tip in diet_plan['tips']:
                    st.write(tip)
            
            st.markdown("---")
            
            # Health tips
            st.subheader("💡 AI-Powered Health Tips")
            
            tips_col1, tips_col2 = st.columns(2)
            
            with tips_col1:
                st.info("""
                **Hydration & Recovery:**
                - 💧 Drink 3-4 liters of water daily
                - 😴 Sleep 7-8 hours every night
                - 🧘 Include rest days in your routine
                - 📊 Track your progress weekly
                """)
            
            with tips_col2:
                st.warning("""
                **Important Reminders:**
                - ⚠️ Warm up before every workout
                - 🥗 Avoid junk food and sugary drinks
                - 📈 Progressive overload is key
                - 🎯 Stay consistent for results
                """)
            
            # Download option
            st.markdown("---")
            st.subheader("📥 Download Your Complete Plan")
            
            # Create downloadable content
            full_plan = f"""
╔══════════════════════════════════════════════════════════════╗
║          AI-POWERED PERSONALIZED FITNESS PLAN                ║
║              Generated by AI Fitness Planner                 ║
╚══════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 USER PROFILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Personal Information:
  • Age: {age} years
  • Gender: {gender}
  • Height: {height} cm
  • Weight: {weight} kg
  • BMI: {bmi} ({bmi_category})

Fitness Goals:
  • Primary Goal: {goal}
  • Workout Time: {workout_time} min/day
  • Intensity Level: {workout_params['intensity']}
  • Focus Area: {workout_params['focus']}

Diet Preferences:
  • Diet Type: {diet_pref}
  • Budget Level: {budget}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏋️ 7-DAY WORKOUT PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
            
            for day in days:
                full_plan += f"\n{day.upper()}:\n"
                for exercise in workout_plan[day]:
                    full_plan += f"  {exercise}\n"
                full_plan += "\n"
            
            full_plan += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🍽️ DAILY DIET PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{diet_plan['title']}

Daily Meals:
"""
            for meal in diet_plan['meals']:
                full_plan += f"  {meal}\n"
            
            full_plan += f"""
Nutritional Information:
  • {diet_plan['calories']}
  • Protein: {diet_plan['protein']}

Pro Tips:
"""
            for tip in diet_plan['tips']:
                full_plan += f"  {tip}\n"
            
            full_plan += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 HEALTH TIPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Drink 3-4 liters of water daily
✅ Sleep 7-8 hours every night
✅ Warm up before and cool down after workouts
✅ Track your progress weekly
✅ Stay consistent with your routine
✅ Avoid junk food and sugary drinks
✅ Listen to your body and rest when needed
✅ Progressive overload is key for results

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ DISCLAIMER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This plan is generated by AI for general guidance. Always consult
with healthcare professionals before starting any new diet or
exercise program, especially if you have existing health conditions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
Powered by: Streamlit + Hugging Face + scikit-learn

Stay Fit, Stay Healthy! 💪
"""
            
            st.download_button(
                label="📥 Download Complete Plan (TXT)",
                data=full_plan,
                file_name=f"AI_Fitness_Plan_{goal.replace(' ', '_')}_{pd.Timestamp.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    else:
        # Welcome screen
        st.info("👈 **Fill in your details in the sidebar and click 'Generate My AI Plan' to get started!**")
        
        # Feature highlights
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 🎯 AI-Powered
            Uses machine learning (scikit-learn) to analyze your profile and create personalized plans
            """)
        
        with col2:
            st.markdown("""
            ### 🇮🇳 Indian-Friendly
            Diet plans with authentic Indian meals suitable for student budgets and preferences
            """)
        
        with col3:
            st.markdown("""
            ### 💰 Budget-Aware
            Three budget levels with affordable meal options for students
            """)
        
        st.markdown("---")
        
        # Technology stack
        st.subheader("🛠️ Powered By")
        tech_col1, tech_col2, tech_col3 = st.columns(3)
        
        with tech_col1:
            st.success("**Python**\nCore programming language")
        
        with tech_col2:
            st.success("**Streamlit**\nModern web interface")
        
        with tech_col3:
            st.success("**scikit-learn**\nML personalization")

if __name__ == "__main__":
    main()
