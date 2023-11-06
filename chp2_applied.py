import pandas as pd
from matplotlib.pyplot import subplots
from pprint import pprint

run = 9
""" 8. College dataset """
if run == 8:
    college = pd.read_csv(
        "/Users/williamhbelew/Desktop/IntroStatsLearning/ISL_labs/data_sets/College.csv")

    # college2 = pd.read_csv(
    #    "/Users/williamhbelew/Desktop/IntroStatsLearning/ISL_labs/data_sets/College.csv", index_col = 0)

    college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
    college3 = college3.set_index('College')

    college = college3

    # pd.plotting.scatter_matrix(college[["Top10perc", "Apps", "Enroll"]])
    # print(college3.describe())
    # print(college3.columns.tolist()[0])
    fig, axes = subplots(2, 2)
    # print(college3.columns)
    #college.boxplot(column='Outstate', by='Private', ax=axes)
    college["Elite"] = pd.cut(college["Top10perc"]/100,
                              [0, 0.5, 1], labels=["No", "Yes"])
    # print(college["Elite"].value_counts())
    #college.boxplot(column='Outstate', by='Elite', ax=axes)
    college.plot.hist(column="Outstate", by="Private", bins=10, ax=axes[0])

    # print(college["Outstate"].values)
    #college.plot.hist(column=['Grad.Rate'], bins=10, ax=axes[1][0])
    college["Grad.Rate"].plot.hist(bins=20, ax=axes[1][0])
    college["Expend"].plot.hist(bins=20, ax=axes[1][1])

if run == 9:
    Auto = pd.read_csv(
        "/Users/williamhbelew/Desktop/IntroStatsLearning/ISL_labs/ISLP_labs/Auto.csv", na_values=['?'])
    Auto_new = Auto.dropna()
    Auto = Auto_new

    # 9a. all vals are quantitative except for year, origin, and name (and 'cylindars' might be more reasonable to treat as qualitative)
    # 9b/c (see comments below)
    nine_d = False

    trimmed_Auto = pd.concat([Auto[:10], Auto[86:]], ignore_index=True)

    # pprint(trimmed_Auto)

    if nine_d == True:
        for col in trimmed_Auto.columns:
            # only quantitative predictors...
            if (col != "name" and col != "origin" and col != "year"):
                # printing range of values for each quant. column
                #print(f"{col}: {Auto[col].min()} <-> {Auto[col].max()}")
                # printing std_dev and mean for each quant. column
                print(
                    f"{col}:\n --> Range: {trimmed_Auto[col].min()} <-> {trimmed_Auto[col].max()}\n --> Standard Deviation: {trimmed_Auto[col].std()}\n --> Mean: {trimmed_Auto[col].mean()}\n")

    nine_e = True
    if nine_e == True:
        fig, axes = subplots(3, 3)
        Auto['origin'].plot.hist(bins=3, ax=axes[0][0])
        Auto.plot.scatter('displacement', 'acceleration', ax=axes[0][1])
        Auto.boxplot(column='acceleration', by='origin', ax=axes[0][2])
        Auto.plot.scatter('weight', 'mpg', ax=axes[1][0])
        Auto.plot.scatter('horsepower', 'mpg', ax=axes[1][1])
        Auto.plot.scatter('displacement', 'mpg', ax=axes[1][2])
        Auto.plot.hist(column='mpg', by='origin', ax=axes[2])

    # 9f. Yes, it seems that:
    # - weight, displacement and horsepower are all INVERSALLY correlated with mpg
    # - origin 1 is inversly correlated with mpg, while origin 3 is positively correlated

    exit()
