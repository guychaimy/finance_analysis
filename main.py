import pandas as pd
import numpy as np

# Create a 3D dataframe
def create_dataframe():
    # columns
    timesteps = ['q1', 'q2', 'q3', 'q4']
    features = ['roi', 'ebida', 'eps']
    stocks = ['APPL', 'MSFT', 'GOOG', 'AMZN', 'META']

    # df dimensions
    n_features = len(features)
    n_timesteps = len(timesteps)
    n_stocks = len(stocks)

    # create the df
    timesteps = np.repeat(timesteps, n_features)
    features = features * n_timesteps
    data = np.array([np.random.randint(10, 99, n_stocks)] * n_features * n_timesteps)
    df = pd.DataFrame(data=data.T, columns=pd.MultiIndex.from_tuples(zip(timesteps, features)), index=stocks)
    print(df)


def main():
    create_dataframe()

if __name__ == '__main__':
    main()