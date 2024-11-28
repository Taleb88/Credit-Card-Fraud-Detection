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


(application_data_condensed_df.
 to_excel('application_data_condensed_df.xlsx', index=False))




'''
def high_schools(df):
    try:
        return df[df['School Type'] == 'HIGH SCHOOL']
    except Exception as e:
        print(f'caught {type(e)}: e \n '
              f'Cannot filter rows')
              
ela_math_science_condensed_high_schools_df = high_schools(ela_math_science_condensed_df)

# high schools only
ela_math_science_condensed_high_schools_df.to_excel(
    'ela_math_science_condensed_high_schools.xlsx',
    index=False
)
              
'''