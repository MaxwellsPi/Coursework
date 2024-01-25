# Prosper Loan Data
## by Edgar Palacios


## Dataset

> The dataset explored here is from Propser.  It contains 113,937 loans and 81 attributes including loan information and personal financial information.


## Summary of Findings
>- Top-four categories include 'Completed', 'Charged-off', 'Defaulted' and 'Cancelled' from most counts to least - respectively.
- Completed loans showed a positive correlation with lower credit ratings while  defaulted and charged-off loans showed a negative correlation.
- Both defaulted and charged-off loans showed debt-to-income ratios above 30% while completed loans were below ~26%.  
- No directional trend is observing for completed loan data.  However, a positive correlation is observed for DTI ratios and decreasing credit grade for defaulted and charged off loans.


## Key Insights for Presentation

> In general, DTI and credit score was a good indicator of whether or not a loan holder would default. While most loans that were granted were completed (69%) an interesting observation was made showing that loan holders who defaulted and had higher credit scores also had significantly elevated DTI ratios.  This was unexpected considering that DTI vs Loan status visualization showed all mean DTI ratios below 40% for all loan status categories.  This indicates that the model used to grant loans may be allowing much higher DTI ratios for applicants with higher credit scores than their low credit score counterparts.  