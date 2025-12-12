# 📝PTSD Relapse Risk Prediction

## Rundown
I made this project to predict the likelihood of relapse in people with PTSD using Linear Regression. I looked at factors like trauma severity, therapy sessions, social support, and comorbidities to see how they influence relapse risk. My goal with this project is to create a data-driven tool that could help clinicians spot high-risk patients early and give them the support they need. 


## Dataset
The dataset `PTSD_Relapse_Risk.csv` is synthetic. I included features that I think could realistically affect relapse risk:

| Feature | Description |
|---------|-------------|
| Age | How old the patient is |
| Gender | Patient gender (Male, Female, Other) |
| Trauma_Severity | How severe their trauma is on a scale from 1–10 |
| Therapy_Sessions_Last_6_Months | How many therapy sessions they had in the last 6 months |
| Social_Support_Score | How strong their social support is, 1–10 |
| Comorbidity_Score | How many other mental health conditions they have |
| Relapse_Risk_Score | The score we’re trying to predict (0–100). Higher = higher risk |


## Here’s what my project does:  
- Predicts a numeric relapse risk score for each patient  
- Converts the numeric score into easy-to-read risk categories: Very Low, Low, Moderate, High, Very High Risk  
- Shows which features matter most in determining risk (so you can see what really influences relapse) 
- Includes visualizations to compare predicted vs actual risk and see the distribution of risk categories 
