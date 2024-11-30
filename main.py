import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
from warnings import simplefilter # suppresses warning, allows > 100 columns to be created in new dataframe
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

application_data_df = pd.read_csv('application_data.csv')
previous_application_df = pd.read_csv('previous_application.csv')

# create condensed version of application_data_df
application_data_condensed_df = pd.DataFrame()
sk_id_curr = application_data_df.iloc[:,0]
application_data_condensed_df['SK_ID_CURR'] = sk_id_curr.copy()
name_contract_type = application_data_df.iloc[:,2]
application_data_condensed_df['NAME_CONTRACT_TYPE'] = name_contract_type.copy()
code_gender = application_data_df.iloc[:,3]
application_data_condensed_df['CODE_GENDER'] = code_gender.copy()
flag_own_car = application_data_df.iloc[:,4]
application_data_condensed_df['FLAG_OWN_CAR'] = flag_own_car.copy()
flag_own_realty = application_data_df.iloc[:,5]
application_data_condensed_df['FLAG_OWN_REALTY'] = flag_own_realty.copy()
cnt_children = application_data_df.iloc[:,6]
application_data_condensed_df['CNT_CHILDREN'] = cnt_children.copy()
amt_income_total = application_data_df.iloc[:,7]
application_data_condensed_df['AMT_INCOME_TOTAL'] = amt_income_total.copy()
amt_credit = application_data_df.iloc[:,8]
application_data_condensed_df['AMT_CREDIT'] = amt_credit.copy()
amt_annuity = application_data_df.iloc[:,9]
application_data_condensed_df['AMT_ANNUITY'] = amt_annuity.copy()
amt_goods_price = application_data_df.iloc[:,10]
application_data_condensed_df['AMT_GOODS_PRICE'] = amt_goods_price.copy()
name_type_suite = application_data_df.iloc[:,11]
application_data_condensed_df['NAME_TYPE_SUITE'] = name_type_suite.copy()
name_income_type = application_data_df.iloc[:,12]
application_data_condensed_df['NAME_INCOME_TYPE'] = name_income_type.copy()
name_education_type = application_data_df.iloc[:,13]
application_data_condensed_df['NAME_EDUCATION_TYPE'] = name_education_type.copy()
name_family_status = application_data_df.iloc[:,14]
application_data_condensed_df['NAME_FAMILY_STATUS'] = name_family_status.copy()
name_housing_type = application_data_df.iloc[:,15]
application_data_condensed_df['NAME_HOUSING_TYPE'] = name_housing_type.copy()
own_car_age = application_data_df.iloc[:,21]
application_data_condensed_df['OWN_CAR_AGE'] = own_car_age.copy()
occupation_type = application_data_df.iloc[:,28]
application_data_condensed_df['OCCUPATION_TYPE'] = occupation_type.copy()
cnt_fam_members = application_data_df.iloc[:,29]
application_data_condensed_df['CNT_FAM_MEMBERS'] = cnt_fam_members.copy()
region_rating_client = application_data_df.iloc[:,30]
application_data_condensed_df['REGION_RATING_CLIENT'] = region_rating_client.copy()
region_rating_client_with_city = application_data_df.iloc[:,31]
application_data_condensed_df['REGION_RATING_CLIENT_W_CITY'] = region_rating_client_with_city.copy()
weekly_approval_process_start = application_data_df.iloc[:,32]
application_data_condensed_df['WEEKDAY_APPR_PROCESS_START'] = weekly_approval_process_start.copy()
hour_approval_process_start = application_data_df.iloc[:,33]
application_data_condensed_df['HOUR_APPR_PROCESS_START'] = hour_approval_process_start.copy()
organization_type = application_data_df.iloc[:,40]
application_data_condensed_df['ORGANIZATION_TYPE'] = organization_type.copy()


(application_data_condensed_df.
 to_excel('application_data_condensed_df.xlsx', index=False))

# creating a new column based on income status per applicant in application_data_condensed_df
application_data_condensed_df['FRAUD_RISK'] = [''] * len(application_data_condensed_df)

application_data_condensed_df.to_excel('application_data_condensed_df.xlsx',
                                      index=False)
# if NAME_INCOME_TYPE is of a certain value, the applicant would be classified as low risk or high risk
status = [] # array reps col values, initially empty but filled in once conditions are met below
for x in application_data_condensed_df['NAME_INCOME_TYPE']:
    try:
        if (x == 'Businessman'
                or x == 'Commercial associate'
                or x == 'Maternity leave'
                or x == 'Pensioner'
                or x == 'State servant'
                or x == 'Student'
                or x == 'Working'):
            status.append('Low Risk')
        elif x == 'Unemployed':
            status.append('High Risk')
        else:
            status.append('Risk = Pending')
            raise ValueError
    except:
        status.append('Invalid Value')
# values added to newly created FRAUD_RISK column
application_data_condensed_df['FRAUD_RISK'] = status

application_data_condensed_df.to_excel('application_data_condensed_df.xlsx',
                                       index=False)

