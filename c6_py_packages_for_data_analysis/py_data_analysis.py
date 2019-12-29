import pandas as pd 
import numpy as np 

df = pd.DataFrame({"a": [1,2,3,4,5], 
        "b": [2,4,np.nan,6,np.nan],
        "c": ['gas', 'diesel', 'diesel', 'gas', 'gas']
    }
)

# if we want to drop missing values inplace
df.dropna(axis=0, inplace=True)

# or we can replace missing values explicitly
b_mean = df.b.mean()
df['b'].replace(np.nan, b_mean, inplace=True)


# creating equal spaced bins using numpy
bins = np.linspace(df.a.min(), df.a.max(), 4)
df['a_bin'] = pd.cut(df.a, bins, include_lowest=True)

# to make dummy variables
c_dummies = pd.get_dummies(df.c)
df = pd.concat([df, c_dummies], axis=1).drop("c", axis=1)


# group by without a new index
df = pd.DataFrame({"a": [1,2,3,4,5], 
        "b": [2,4,np.nan,6,np.nan],
        "c": ['gas', 'diesel', 'diesel', 'gas', 'gas']
    }
)
df.groupby("c", as_index=False).mean()


# pandas pivot
# set new index= and new columns=
df.groupby("c", as_index=False).mean().pivot("c", "a")


