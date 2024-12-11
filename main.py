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

# +===================+
# if NAME_INCOME_TYPE is of a certain value, the applicant would be
#   classified as low risk or high risk
# +===================+
status = [] # array reps col values, initially empty but filled in once conditions are met below
for x in application_data_condensed_df['NAME_INCOME_TYPE']:
    try:
        if (x == 'Businessman'
                or x == 'Commercial associate'
                or x == 'Maternity leave'
                or x == 'Pensioner'
                or x == 'State servant'
                or x == 'Working'):
            status.append('Low Risk')
        elif x == 'Student':
            status.append('Medium Risk')
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

'''
# filling in empty values under own car age
application_data_condensed_df = (
    application_data_condensed_df['OWN_CAR_AGE'].replace('', 0))

application_data_condensed_df.to_excel('application_data_condensed_df.xlsx',
                                       index=False)
'''

# +===================+
# filtering based on certain conditions
# +===================+

# unemployed applicants only
def unemployed_applicants(df):
    try:
        return df[df['NAME_INCOME_TYPE'] == 'Unemployed']
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

application_data_condensed_unemployed_applicants_df = \
    unemployed_applicants(application_data_condensed_df)

application_data_condensed_unemployed_applicants_df.to_excel(
    'application_data_condensed_unemployed_applicants_df.xlsx',
    index=False)

# businessman applicants only
def businessman_applicants(df):
    try:
        return df[df['NAME_INCOME_TYPE'] == 'Businessman']
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

application_data_condensed_businessman_applicants_df = \
    businessman_applicants(application_data_condensed_df)

application_data_condensed_businessman_applicants_df.to_excel(
    'application_data_condensed_businessman_applicants_df.xlsx',
    index=False)

# commercial associate applicants only
def commercial_associate_applicants(df):
    try:
        return df[df['NAME_INCOME_TYPE'] == 'Commercial Associate']
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

application_data_condensed_commercial_associate_applicants_df = \
    commercial_associate_applicants(application_data_condensed_df)

application_data_condensed_commercial_associate_applicants_df.to_excel(
    'application_data_condensed_commercial_associate_applicants_df.xlsx',
    index=False)

# maternity leave applicants only
def maternity_leave_applicants(df):
    try:
        return df[df['NAME_INCOME_TYPE'] == 'Maternity leave']
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

application_data_condensed_maternity_leave_applicants_df = \
    maternity_leave_applicants(application_data_condensed_df)

application_data_condensed_maternity_leave_applicants_df.to_excel(
    'application_data_condensed_maternity_leave_applicants_df.xlsx',
    index=False)

# pensioner applicants only
def pensioner_applicants(df):
    try:
        return df[df['NAME_INCOME_TYPE'] == 'Pensioner']
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

application_data_condensed_pensioner_applicants_df = \
    pensioner_applicants(application_data_condensed_df)

application_data_condensed_pensioner_applicants_df.to_excel(
    'application_data_condensed_pensioner_applicants_df.xlsx',
    index=False)

# state servant applicants only
def state_servant_applicants(df):
    try:
        return df[df['NAME_INCOME_TYPE'] == 'State servant']
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

application_data_condensed_state_servant_applicants_df = \
    state_servant_applicants(application_data_condensed_df)

application_data_condensed_state_servant_applicants_df.to_excel(
    'application_data_condensed_state_servant_applicants_df.xlsx',
    index=False)

# student applicants only
def student_applicants(df):
    try:
        return df[df['NAME_INCOME_TYPE'] == 'Student']
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

application_data_condensed_student_applicants_df = \
    student_applicants(application_data_condensed_df)

application_data_condensed_student_applicants_df.to_excel(
    'application_data_condensed_student_applicants_df.xlsx',
    index=False)

# working applicants only
def working_applicants(df):
    try:
        return df[df['NAME_INCOME_TYPE'] == 'Working']
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

application_data_condensed_working_applicants_df = \
    working_applicants(application_data_condensed_df)

application_data_condensed_working_applicants_df.to_excel(
    'application_data_condensed_working_applicants_df.xlsx',
    index=False)

# unemployed with children applicants only
def unemployed_with_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Unemployed') & (df['CNT_CHILDREN'] > 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

unemployed_with_children_applicants_df = unemployed_with_children_applicants(application_data_df)

unemployed_with_children_applicants_df.to_excel('unemployed_with_children_applicants_df.xlsx',
                                                index=False)

# unemployed without children
def unemployed_without_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Unemployed') & (df['CNT_CHILDREN'] == 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

unemployed_without_children_applicants_df = unemployed_without_children_applicants(application_data_df)

unemployed_without_children_applicants_df.to_excel('unemployed_without_children_applicants_df.xlsx',
                                                index=False)

# businessman with children applicants only
def businessman_with_children_applicants(df):
    try:    
        return df[(df['NAME_INCOME_TYPE'] == 'Businessman') & (df['CNT_CHILDREN'] > 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

businessman_with_children_applicants_df = businessman_with_children_applicants(application_data_df)

businessman_with_children_applicants_df.to_excel('businessman_with_children_applicants_df.xlsx',
                                                index=False)

# businessman without children
def businessman_without_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Businessman') & (df['CNT_CHILDREN'] == 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')    

businessman_without_children_applicants_df = businessman_without_children_applicants(application_data_df)

businessman_without_children_applicants_df.to_excel('businessman_without_children_applicants_df.xlsx',
                                                index=False)

# commercial associate with children applicants only
def commercial_associate_with_children_applicants(df):
    try:    
        return df[(df['NAME_INCOME_TYPE'] == 'Commercial associate') & (df['CNT_CHILDREN'] > 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

commercial_associate_with_children_applicants_df = commercial_associate_with_children_applicants(application_data_df)

commercial_associate_with_children_applicants_df.to_excel('commercial_associate_with_children_applicants_df.xlsx',
                                                index=False)

# commercial_associate without children
def commercial_associate_without_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Commercial associate') & (df['CNT_CHILDREN'] == 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')
            
commercial_associate_without_children_applicants_df = commercial_associate_without_children_applicants(application_data_df)

commercial_associate_without_children_applicants_df.to_excel('commercial_associate_without_children_applicants_df.xlsx',
                                                index=False)

# maternity leave with children applicants only
def maternity_leave_with_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Maternity leave') & (df['CNT_CHILDREN'] > 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')    

maternity_leave_with_children_applicants_df = maternity_leave_with_children_applicants(application_data_df)

maternity_leave_with_children_applicants_df.to_excel('maternity_leave_with_children_applicants_df.xlsx',
                                                index=False)

# maternity_leave without children
def maternity_leave_without_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Maternity leave') & (df['CNT_CHILDREN'] == 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')
        
maternity_leave_without_children_applicants_df = maternity_leave_without_children_applicants(application_data_df)

maternity_leave_without_children_applicants_df.to_excel('maternity_leave_without_children_applicants_df.xlsx',
                                                index=False)

# pensioner with children applicants only
def pensioner_with_children_applicants(df):
    try:    
        return df[(df['NAME_INCOME_TYPE'] == 'Pensioner') & (df['CNT_CHILDREN'] > 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

pensioner_with_children_applicants_df = pensioner_with_children_applicants(application_data_df)

pensioner_with_children_applicants_df.to_excel('pensioner_with_children_applicants_df.xlsx',
                                                index=False)

# pensioner without children
def pensioner_without_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Pensioner') & (df['CNT_CHILDREN'] == 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')    

pensioner_without_children_applicants_df = pensioner_without_children_applicants(application_data_df)

pensioner_without_children_applicants_df.to_excel('pensioner_without_children_applicants_df.xlsx',
                                                index=False)

# state servant with children applicants only
def state_servant_with_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'State servant') & (df['CNT_CHILDREN'] > 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

state_servant_with_children_applicants_df = state_servant_with_children_applicants(application_data_df)

state_servant_with_children_applicants_df.to_excel('state_servant_with_children_applicants_df.xlsx',
                                                index=False)

# state servant without children
def state_servant_without_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'State servant') & (df['CNT_CHILDREN'] == 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

state_servant_without_children_applicants_df = state_servant_without_children_applicants(application_data_df)

state_servant_without_children_applicants_df.to_excel('state_servant_without_children_applicants_df.xlsx',
                                                index=False)

# student with children applicants only
def student_with_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Student') & (df['CNT_CHILDREN'] > 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')
    
student_with_children_applicants_df = student_with_children_applicants(application_data_df)

student_with_children_applicants_df.to_excel('student_with_children_applicants_df.xlsx',
                                                index=False)

# student without children
def student_without_children_applicants(df):
    try:    
        return df[(df['NAME_INCOME_TYPE'] == 'Student') & (df['CNT_CHILDREN'] == 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')

student_without_children_applicants_df = student_without_children_applicants(application_data_df)

student_without_children_applicants_df.to_excel('student_without_children_applicants_df.xlsx',
                                                index=False)

# working with children applicants only
def working_with_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Working') & (df['CNT_CHILDREN'] > 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')    

working_with_children_applicants_df = working_with_children_applicants(application_data_df)

working_with_children_applicants_df.to_excel('working_with_children_applicants_df.xlsx',
                                                index=False)

# working without children
def working_without_children_applicants(df):
    try:
        return df[(df['NAME_INCOME_TYPE'] == 'Working') & (df['CNT_CHILDREN'] == 0)]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot filter rows')    

working_without_children_applicants_df = working_without_children_applicants(application_data_df)

working_without_children_applicants_df.to_excel('working_without_children_applicants_df.xlsx',
                                                index=False)


# +===================+
# pivot tables
# +===================+
# unemployed applicants annuity avg pivot table
unemployed_applicants_annuity_avg_df = \
    pd.pivot_table(application_data_condensed_unemployed_applicants_df,
                                                index= "CODE_GENDER",
                                                values='AMT_ANNUITY',
                                                columns='NAME_FAMILY_STATUS',
                                                aggfunc='mean'
                                                )

unemployed_applicants_annuity_avg_df.\
    to_excel('unemployed_applicants_annuity_avg_pivot_table.xlsx')

# businessman applicants annuity avg pivot table
businessman_applicants_annuity_avg_df = \
    pd.pivot_table(application_data_condensed_businessman_applicants_df,
                                                index= "CODE_GENDER",
                                                values='AMT_ANNUITY',
                                                columns='NAME_FAMILY_STATUS',
                                                aggfunc='mean'
                                                )

businessman_applicants_annuity_avg_df.\
    to_excel('businessman_applicants_annuity_avg_pivot_table.xlsx')

# commercial associate applicants annuity avg pivot table
commercial_associate_applicants_annuity_avg_df = \
    pd.pivot_table(application_data_condensed_commercial_associate_applicants_df,
                                                index= "CODE_GENDER",
                                                values='AMT_ANNUITY',
                                                columns='NAME_FAMILY_STATUS',
                                                aggfunc='mean'
                                                )

commercial_associate_applicants_annuity_avg_df.\
    to_excel('commercial_associate_applicants_annuity_avg_pivot_table.xlsx')

# maternity leave applicants annuity avg pivot table
maternity_leave_applicants_annuity_avg_df = \
    pd.pivot_table(application_data_condensed_maternity_leave_applicants_df,
                                                index= "CODE_GENDER",
                                                values='AMT_ANNUITY',
                                                columns='NAME_FAMILY_STATUS',
                                                aggfunc='mean'
                                                )

maternity_leave_applicants_annuity_avg_df.\
    to_excel('maternity_leave_applicants_annuity_avg_pivot_table.xlsx')

# pensioner applicants annuity avg pivot table
pensioner_applicants_annuity_avg_df = \
    pd.pivot_table(application_data_condensed_pensioner_applicants_df,
                                                index= "CODE_GENDER",
                                                values='AMT_ANNUITY',
                                                columns='NAME_FAMILY_STATUS',
                                                aggfunc='mean'
                                                )

pensioner_applicants_annuity_avg_df.\
    to_excel('pensioner_applicants_annuity_avg_pivot_table.xlsx')

# state servant applicants annuity avg pivot table
state_servant_applicants_annuity_avg_df = \
    pd.pivot_table(application_data_condensed_state_servant_applicants_df,
                                                index= "CODE_GENDER",
                                                values='AMT_ANNUITY',
                                                columns='NAME_FAMILY_STATUS',
                                                aggfunc='mean'
                                                )

state_servant_applicants_annuity_avg_df.\
    to_excel('state_servant_applicants_annuity_avg_pivot_table.xlsx')

# student applicants annuity avg pivot table
student_applicants_annuity_avg_df = \
    pd.pivot_table(application_data_condensed_student_applicants_df,
                                                index= "CODE_GENDER",
                                                values='AMT_ANNUITY',
                                                columns='NAME_FAMILY_STATUS',
                                                aggfunc='mean'
                                                )

student_applicants_annuity_avg_df.\
    to_excel('student_applicants_annuity_avg_pivot_table.xlsx')

# working applicants annuity avg pivot table
working_applicants_annuity_avg_df = \
    pd.pivot_table(application_data_condensed_working_applicants_df,
                                                index= "CODE_GENDER",
                                                values='AMT_ANNUITY',
                                                columns='NAME_FAMILY_STATUS',
                                                aggfunc='mean'
                                                )

working_applicants_annuity_avg_df.\
    to_excel('working_applicants_annuity_avg_pivot_table.xlsx')


# +===================+
# charts to be developed here
# +===================+

application_data_condensed_unemployed_applicants_df.plot.barh(
    x='SK_ID_CURR',
    y='AMT_ANNUITY',
    title='Annuity Amount per Applicant',
    color='green'
)
plt.xlabel('Annuity Amounts')
plt.show() # produces bar graph

application_data_condensed_businessman_applicants_df.plot.barh(
    x='SK_ID_CURR',
    y='AMT_ANNUITY',
    title='Annuity Amount per Applicant',
    color='green'
)
plt.xlabel('Annuity Amounts')
plt.show() # produces bar graph
'''
application_data_condensed_commercial_associate_applicants_df.plot.barh(
    x='SK_ID_CURR',
    y='AMT_ANNUITY',
    title='Annuity Amount per Applicant',
    color='green'
)
plt.xlabel('Annuity Amounts')
plt.show() # bar graph should be produced, but data is too big
'''
application_data_condensed_maternity_leave_applicants_df.plot.barh(
    x='SK_ID_CURR',
    y='AMT_ANNUITY',
    title='Annuity Amount per Applicant',
    color='green'
)
plt.xlabel('Annuity Amounts')
plt.show() # produces bar graph
'''
application_data_condensed_pensioner_applicants_df.plot.barh(
    x='SK_ID_CURR',
    y='AMT_ANNUITY',
    title='Annuity Amount per Applicant',
    color='green'
)
plt.xlabel('Annuity Amounts')
plt.show() # bar graph should be produced, but data is too big

application_data_condensed_state_servant_applicants_df.plot.barh(
    x='SK_ID_CURR',
    y='AMT_ANNUITY',
    title='Annuity Amount per Applicant',
    color='green'
)
plt.xlabel('Annuity Amounts')
plt.show() # bar graph should be produced, but data is too big
'''
application_data_condensed_student_applicants_df.plot.barh(
    x='SK_ID_CURR',
    y='AMT_ANNUITY',
    title='Annuity Amount per Applicant',
    color='green'
)
plt.xlabel('Annuity Amounts')
plt.show() # produces bar graph
'''
application_data_condensed_working_applicants_df.plot.barh(
    x='SK_ID_CURR',
    y='AMT_ANNUITY',
    title='Annuity Amount per Applicant',
    color='green'
)
plt.xlabel('Annuity Amounts')
plt.show() # bar graph should be produced, but data is too big
'''


# +===================+
# conditional formatting implemented based on certain conditions
# +===================+

# background color of fraud risk based on level
def risk_color(risk_level):
    try:
        if risk_level == 'High Risk':
            return ('background-color: red; '
                    'font-weight: bold; '
                    'color: black')
        elif risk_level == 'Medium Risk':
            return 'background-color: yellow'
        elif risk_level == 'Low Risk':
            return 'background-color: #00FF7F'
        else:
            return 'background-color: #FFFFFF'
    except:
        print('Error - Cannot fill in background color of cells')

application_data_condensed_styled_df = (
    application_data_condensed_df.
    style.
    applymap(risk_color, subset=['FRAUD_RISK'])
)

application_data_condensed_styled_df.\
    to_excel('application_data_condensed_df.xlsx',
                                       index=False)


# +===================+
# merging certain datasets
# +===================+

#merge student applicants + unemployed applicants based on day/time
student_and_unemployed_applicants_merge_df = pd.merge(
    application_data_condensed_student_applicants_df, 
    application_data_condensed_unemployed_applicants_df,
    on=['WEEKDAY_APPR_PROCESS_START', 'HOUR_APPR_PROCESS_START'] #   
)

student_and_unemployed_applicants_merge_df.\
    to_excel('student_and_unemployed_applicants_merge_df.xlsx', 
             index=False)

def highlight_weekday_and_hour(self):
    try:
        return 'background-color: yellow'
    except:
        print('Error - Cannot fill in background color of cells')

student_and_unemployed_applicants_merge_styled_df = (
    student_and_unemployed_applicants_merge_df.
    style.
    applymap(highlight_weekday_and_hour, subset=['WEEKDAY_APPR_PROCESS_START',
                                 'HOUR_APPR_PROCESS_START'])
)

student_and_unemployed_applicants_merge_styled_df.\
    to_excel('student_and_unemployed_applicants_merge_styled_df.xlsx', 
             index=False)