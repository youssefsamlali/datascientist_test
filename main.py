# /datascientist/main.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create pandas dataframes
transactions = pd.read_csv('data/transactions.csv', sep=';')
products = pd.read_csv('data/products.csv', sep=';')
# Question 1 :
def dataframe_audit(df):
    # simple function showing dataframe infos and describe
    print(df.info())
    print(df.describe())
def check_dates(df) :
    # function converting string type dates to datetime format dates and check anomalies
    print('**************Check Date Formats**************')
    if pd.to_datetime(transactions['transaction_date'], format='%d/%m/%Y').isnull().any() == False :
        return 'looks Great :)'
    return 'Error in converting date format'
# Question 2
def compute_turnover(transactions, products) :
    # Computing turnover per week of the products of CATEG_1 in 2018
    df = pd.merge(transactions,products,on='product_id',how='left')
    df['transaction_date'] = pd.to_datetime(transactions['transaction_date'], format='%d/%m/%Y')
    df = df.loc[(df.transaction_date.dt.year == 2018) & (df.category == 'CATEG_1')]
    turnover = df.resample('W', on='transaction_date').sum().reset_index().sort_values(by='transaction_date')[['transaction_date','spend_amount']]
    print(turnover)
    #plt.plot('transaction_date', 'spend_amount' , data=turnover)
    #plt.show()

# Question 5
def filtering_df(transactions, products):
    # applies the necessary filters to the dataframe and returns a new one
    df = pd.merge(transactions, products, on='product_id', how='left')
    df['transaction_date'] = pd.to_datetime(transactions['transaction_date'], format='%d/%m/%Y')
    df = df.loc[(df.brand == 'BRAND_2') & (df.category == 'CATEG_2') & (
                (df.store_id == 1) | (df.store_id == 2) | (df.store_id == 3) | (df.store_id == 4) | (df.store_id == 5))]
    return df
# Question 6 :
def compute_commercial_equation(df):
    # calculate the commercial equation per week
    df = df.resample('W', on='transaction_date').agg({'spend_amount': 'sum',
                                                      'client_id': lambda x: x.nunique(),
                                                      'quantity': ['sum', lambda x: (x >= 1).sum()]})
    df.columns = ["_".join(pair) for pair in df.columns]
    df = df.rename(columns={'spend_amount_sum': 'turnover', 'client_id_<lambda>': 'nb_of_clients',
                            'quantity_sum': 'quantity_purchased', 'quantity_<lambda_0>': 'nb_of_checkouts'})
    return df
def commercial_indicators(df):
    # calcultate commercial levers
    df['avg_revenue_per_checkout'] = df['turnover'] / df['nb_of_checkouts']
    df['avg_sales_per_customer'] = df['quantity_purchased'] / df['nb_of_clients']
    df['avg_revenue_per_quantity_purchased'] = df['turnover'] / df['quantity_purchased']
    df['avg_nb_checkouts_per_customer'] = df['nb_of_checkouts'] / df['nb_of_clients']
    df['avg_nb_of_quantities_per_checkout'] = df['quantity_purchased'] / df['nb_of_checkouts']
    return df
# Question 7 :
def period_highlight(df):
    df = df.tail(8).reset_index()
    df.index = ['P1', 'P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P2']
    df = df.reset_index()
    df = df.rename(columns={'index': 'period'})
    df = df.groupby(by='period').mean()
    df = df.T
    df['percent'] = (df['P2']/df['P1']-1)*100
    print(df)
def reactivation_target():
    # identify the reactivation target
    df = pd.merge(transactions, products, on='product_id', how='left')
    df['transaction_date'] = pd.to_datetime(transactions['transaction_date'], format='%d/%m/%Y')
    df['week'] = df.transaction_date.dt.strftime("%V").astype(int)
    df['period'] = df['week'].apply(lambda x: 'P1' if x < 36 else 'P2')
    p2_coustomers = df[(df.category == 'CATEG_2') & (df.brand == 'BRAND_2') & (df.period == 'P2')].client_id.unique()
    number_clients = df[(df.category=='CATEG_2') & (df.brand=='BRAND_2') & (df.period=='P1') & (~df.client_id.isin(p2_coustomers))].client_id.nunique()
    return number_clients

def loyal_target() :
    # identify the loyal target
    df = pd.merge(transactions, products, on='product_id', how='left')
    df['transaction_date'] = pd.to_datetime(transactions['transaction_date'], format='%d/%m/%Y')
    buying_other_brands = df[(df.category == 'CATEG_2') & (df.brand != 'BRAND_2')].client_id.unique()
    number_clients = df[(df.duplicated(['client_id'], keep='first')) & (df.category == 'CATEG_2') & (
        ~df.client_id.isin(buying_other_brands))].client_id.nunique()
    return number_clients

def compute_avg_turnover_customer() :
    # Computing average turnover per customer of the products of CATEG_2 on brand2
    df = pd.merge(transactions,products,on='product_id',how='left')
    df['transaction_date'] = pd.to_datetime(transactions['transaction_date'], format='%d/%m/%Y')
    df = df.loc[(df.brand == 'BRAND_2') & (df.category == 'CATEG_2')]
    avg_turnover_per_customer = df.spend_amount.sum()/df.client_id.nunique()
    return avg_turnover_per_customer
if __name__ == "__main__":
    dataframe_audit(transactions)
    print(check_dates(transactions))
    dataframe_audit(products)
    # Question 2
    compute_turnover(transactions, products)
    # Question 5 :
    df = filtering_df(transactions, products)
    # Question 6 :
    df = compute_commercial_equation(df)
    # Question 7 :
    df = commercial_indicators(df)
    period_highlight(df)
    print('number of clients in reactivation target :', reactivation_target())
    print('number of clients in loyal target :', loyal_target())
    print('turnover on brand 2 within category 2 :', compute_avg_turnover_customer() )


