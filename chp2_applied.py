import pandas as pd
from matplotlib.pyplot import subplots

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

college.plot.hist(column='Top10perc', by='Room.Board', bins=10, ax=axes[1])


exit()
