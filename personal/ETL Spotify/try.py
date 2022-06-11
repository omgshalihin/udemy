import pandas as pd

first_name = ['Linda', 'Steve', 'Henry', 'Sara']
gender = ['female', 'male', 'male', 'female']
salary_usd = [3000, 5000, 12000, 5000]

customer_dict = {'first_name':first_name, 'gender':gender, 'salary_usd':salary_usd}
print(customer_dict)

df = pd.DataFrame(customer_dict)
print(df)

# Print the first two rows of the DataFrame
print(df[:2])

# Subset the DataFrame for gender "female"
print(df[df['gender'] == 'female'])

# Select only the columns of interest
print(df[['gender', 'salary_usd']])

# Subset the DataFrame for salary_usd ">3000"
print(df[df['salary_usd'] > 3000])

