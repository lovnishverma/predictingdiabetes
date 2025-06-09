# Diabetes Prediction Web Application

A Flask-based web application that predicts diabetes risk using machine learning. The application uses Logistic Regression to assess diabetes probability based on key health indicators including age, medical history, BMI, HbA1c levels, and blood glucose levels.

## Features

- **Medical Prediction**: AI-powered diabetes risk assessment
- **Input Validation**: Comprehensive form validation for all health parameters
- **Health Metrics**: Uses clinically relevant indicators for accurate predictions
- **Error Handling**: Robust error management and user feedback
- **Real-time Results**: Instant diabetes risk evaluation

## Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn (Logistic Regression)
- **Data Processing**: pandas, numpy
- **Frontend**: HTML templates (Jinja2)
- **Dataset**: Diabetes health indicators (CSV format)

## Project Structure

```
diabetes-predictor/
│
├── app.py                # Main Flask application
├── te.csv               # Diabetes dataset (without headers)
├── templates/
│   └── index.html       # Main page with form and results
├── static/              # CSS, JS, images (if any)
└── README.md           # Project documentation
```

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/lovnishverma/predictingdiabetes.git
cd predictingdiabetes
```

### Step 2: Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

### Step 3: Prepare the Dataset

Ensure `te.csv` is in the root directory with 7 columns (no headers):
- Column 1: Age (years)
- Column 2: Hypertension (0=No, 1=Yes)
- Column 3: Heart Disease (0=No, 1=Yes)
- Column 4: BMI (Body Mass Index)
- Column 5: HbA1c Level (Hemoglobin A1c percentage)
- Column 6: Blood Glucose Level (mg/dL)
- Column 7: Diabetes Status (0=No Diabetes, 1=Diabetes)

### Step 4: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage

1. **Access Application**: Navigate to `http://localhost:5000`
2. **Enter Health Data**: Fill in all required health parameters
3. **Submit Form**: Click predict to get diabetes risk assessment
4. **View Results**: See prediction result (0=No Diabetes, 1=Diabetes Risk)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main page with diabetes prediction form |
| `/` | POST | Process health data and return diabetes prediction |

## Model Details

- **Algorithm**: Logistic Regression
- **Features**: Age, Hypertension, Heart Disease, BMI, HbA1c Level, Blood Glucose Level
- **Target**: Diabetes Status (Binary Classification)
- **Training**: Model trains on entire dataset for each prediction

## Input Parameters

### Required Health Indicators

| Parameter | Type | Range/Values | Description |
|-----------|------|--------------|-------------|
| **Age** | Float | 0-120 years | Patient's age in years |
| **Hypertension** | Integer | 0=No, 1=Yes | High blood pressure diagnosis |
| **Heart Disease** | Integer | 0=No, 1=Yes | Cardiovascular disease history |
| **BMI** | Float | 10.0-50.0+ | Body Mass Index (kg/m²) |
| **HbA1c Level** | Float | 3.5-15.0+ | Hemoglobin A1c percentage |
| **Blood Glucose Level** | Float | 80-400+ mg/dL | Blood sugar level |

### Clinical Reference Ranges

#### BMI Categories
- **Underweight**: < 18.5
- **Normal**: 18.5 - 24.9
- **Overweight**: 25.0 - 29.9
- **Obese**: ≥ 30.0

#### HbA1c Levels
- **Normal**: < 5.7%
- **Prediabetes**: 5.7% - 6.4%
- **Diabetes**: ≥ 6.5%

#### Blood Glucose (Fasting)
- **Normal**: 70-100 mg/dL
- **Prediabetes**: 100-125 mg/dL
- **Diabetes**: ≥ 126 mg/dL

## Sample Input Examples

### High Risk Profile
```
Age: 55
Hypertension: 1 (Yes)
Heart Disease: 1 (Yes)
BMI: 32.5
HbA1c Level: 7.2
Blood Glucose Level: 180
Expected Result: 1 (High Diabetes Risk)
```

### Moderate Risk Profile
```
Age: 45
Hypertension: 1 (Yes)
Heart Disease: 0 (No)
BMI: 28.0
HbA1c Level: 6.0
Blood Glucose Level: 110
Expected Result: Variable (depends on model)
```

### Low Risk Profile
```
Age: 25
Hypertension: 0 (No)
Heart Disease: 0 (No)
BMI: 22.0
HbA1c Level: 5.2
Blood Glucose Level: 90
Expected Result: 0 (Low Diabetes Risk)
```

## Prediction Results

- **0**: No Diabetes Risk / Normal ✅
- **1**: Diabetes Risk Detected ⚠️

## Key Risk Factors

### Primary Indicators (Strong Predictors)
1. **HbA1c Level**: Most reliable long-term glucose indicator
2. **Blood Glucose Level**: Direct measure of current blood sugar
3. **BMI**: Obesity strongly correlates with Type 2 diabetes
4. **Age**: Risk increases with age, especially after 45

### Secondary Indicators (Contributing Factors)
1. **Hypertension**: Often co-occurs with diabetes
2. **Heart Disease**: Shares risk factors with diabetes

## Dataset Format

The `te.csv` file should contain numerical data without headers:

```csv
45,1,0,28.5,6.2,140,1
32,0,0,23.1,5.1,95,0
60,1,1,35.2,8.1,200,1
...
```

## Input Validation Features

The application includes comprehensive validation:

- **Required Fields Check**: All 6 health parameters must be provided
- **Data Type Validation**: Ensures proper float/integer conversion
- **Error Handling**: Graceful handling of prediction errors
- **User Feedback**: Clear error messages for missing inputs

## Model Performance Considerations

### Advantages of Logistic Regression
- Interpretable coefficients for each health factor
- Probability estimates for risk assessment
- Fast training and prediction
- Works well with medical diagnostic features

### Limitations
- Linear decision boundary may miss complex interactions
- Assumes independence between features
- May need feature scaling for optimal performance

## Improvement Suggestions

### 1. Model Enhancement
```python
# Add feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Add cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)

# Show prediction probability
probability = model.predict_proba(input_array)[0]
confidence = max(probability) * 100
```

### 2. Additional Features
- **Family History**: Genetic predisposition indicator
- **Physical Activity**: Exercise frequency and intensity
- **Diet Habits**: Nutrition and eating patterns
- **Smoking Status**: Tobacco use history
- **Waist Circumference**: Additional obesity measure

### 3. Enhanced Validation
```python
def enhanced_validation(data):
    # Age validation
    if not (0 <= data['age'] <= 120):
        return False, "Age must be between 0 and 120"
    
    # BMI validation
    if not (10 <= data['bmi'] <= 60):
        return False, "BMI must be between 10 and 60"
    
    # HbA1c validation
    if not (3.0 <= data['HbA1c_level'] <= 15.0):
        return False, "HbA1c must be between 3.0 and 15.0"
    
    return True, "Valid"
```

### 4. User Experience Improvements
- **Risk Interpretation**: Explain what the prediction means
- **Health Recommendations**: Provide actionable advice
- **Trend Tracking**: Allow users to save and track results over time
- **Educational Content**: Include diabetes prevention information

### 5. Clinical Integration
- **Reference Ranges**: Display normal vs. abnormal ranges
- **Risk Stratification**: Low/Medium/High risk categories
- **Screening Guidelines**: When to consult healthcare providers
- **Lifestyle Recommendations**: Diet and exercise suggestions

## Medical Disclaimer & Ethics

### Important Medical Considerations
- **Not a Diagnostic Tool**: Results are for screening purposes only
- **Professional Consultation**: Always consult healthcare providers
- **Individual Variation**: Results may not apply to all populations
- **Regular Monitoring**: Diabetes risk can change over time

### Recommended Practices
- Clear disclaimer about medical advice limitations
- Encourage professional medical consultation
- Regular model validation with clinical data
- Compliance with healthcare data regulations (HIPAA)

## Security & Privacy

### Data Protection
- No storage of personal health information
- Secure handling of sensitive medical data
- HTTPS encryption for data transmission
- Compliance with healthcare privacy laws

### Implementation Notes
```python
# Add session-based security
from flask import session
import secrets

# Generate secure session keys
app.secret_key = secrets.token_hex(16)

# Log predictions without personal data
import logging
logging.info(f"Prediction made: {result} at {datetime.now()}")
```

## Troubleshooting

### Common Issues

1. **Import Errors**:
   ```bash
   pip install flask pandas numpy scikit-learn
   ```

2. **CSV Format Issues**:
   - Ensure 7 columns with no headers
   - All values should be numeric
   - Check for missing values

3. **Validation Errors**:
   - Verify all form fields are filled
   - Check data type consistency
   - Ensure reasonable value ranges

4. **Model Training Issues**:
   - Sufficient training samples needed
   - Balanced dataset (diabetes vs. non-diabetes cases)
   - Check for data quality issues

## Performance Optimization

```python
# Cache trained model
import joblib
from functools import lru_cache

@lru_cache(maxsize=1)
def get_trained_model():
    model = joblib.load('diabetes_model.pkl')
    return model

# Batch predictions for multiple users
def batch_predict(user_data_list):
    model = get_trained_model()
    predictions = model.predict(user_data_list)
    return predictions
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/medical-enhancement`)
3. Commit changes (`git commit -am 'Add clinical feature'`)
4. Push to branch (`git push origin feature/medical-enhancement`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Medical Resources

- **American Diabetes Association**: https://diabetes.org
- **CDC Diabetes Prevention Program**: https://cdc.gov/diabetes
- **World Health Organization Diabetes**: https://who.int/diabetes

## Contact

For questions, medical feedback, or technical support, please open an issue in the repository.

---

**⚠️ IMPORTANT MEDICAL DISCLAIMER**: This application is for educational and screening purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read or seen in this application.
