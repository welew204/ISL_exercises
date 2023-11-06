from ISLP import load_data
from pprint import pprint
from matplotlib.pyplot import subplots
import pandas as pd



run = 10

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

""" 9. Auto dataset """
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

    nine_e = False
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
    """ 10. Boston (housing) data set """
if run == 10:
    # 10a
    Boston = load_data('Boston')
    #pprint(Boston)
    # 10b - rows are suburbs of Boston, columns are:
    """ crim: per capita crime rate by town.
    zn: proportion of residential land zoned for lots over 25,000 sq.ft.
    indus: proportion of non-retail business acres per town.
    chas: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).
    nox: nitrogen oxides concentration (parts per 10 million).
    rm: average number of rooms per dwelling.
    age: proportion of owner-occupied units built prior to 1940.
    dis: weighted mean of distances to five Boston employment centres.
    rad: index of accessibility to radial highways.
    tax: full-value property-tax rate per $10,000.
    ptratio: pupil-teacher ratio by town.
    lstat: lower status of the population (percent).
    medv: median value of owner-occupied homes in $1000s.
    """
    # 10c/d.... crime seems inversly correlated to 'dis', 'medv' and positively correlated (sort of) to 'ptration', 'nox', 'lstat'    fig, axes = subplots(2,3)
    plot = False
    if plot == True:
        Boston.plot.scatter('indus', 'crim', ax=axes[0][0])
        Boston.plot.scatter('dis', 'crim', ax=axes[0][1])
        Boston.plot.scatter('nox', 'crim', ax=axes[0][2])
        Boston.plot.scatter('lstat', 'crim', ax=axes[1][0])
        Boston.plot.scatter('medv', 'crim', ax=axes[1][1])
    
    # 10e. find 5 highest crime, tax, p/t ratio
    # the range of Taxation is WILD (large)
    ten_e = False
    if ten_e:
        top_crime_neighborhoods = Boston.nlargest(5, columns=['crim'])
        top_tax_neighborhoods = Boston.nlargest(5, columns=['tax'])
        top_ptratio_neighborhoods = Boston.nlargest(5, columns=['ptratio'])
        print(f"Range of CRIME vals: {Boston['crim'].min()} <--> {Boston['crim'].max()}")
        print(top_crime_neighborhoods)
        print(f"Range of TAX vals: {Boston['tax'].min()} <--> {Boston['tax'].max()}")
        print(top_tax_neighborhoods)
        print(f"Range of P/T Ratio vals: {Boston['ptratio'].min()} <--> {Boston['ptratio'].max()}")
        print(top_ptratio_neighborhoods)
    ten_f = False
    if ten_f:
        print("Suburbs that bound the Charles: ", len(Boston.loc[lambda df: df["chas"] == 1]))
    
    ten_g = False
    if ten_g:
        charles_facing = Boston.loc[lambda df: df["chas"] == 1]
        #10g... median p/t ratio for suburbs facing the charles
        print(charles_facing["ptratio"].median())
        # ... compared to median of overall data set
        print(Boston["ptratio"].median())

    ten_h = False
    if ten_h:
        lowest_med_owner_occupied = Boston.nsmallest(1, columns=["medv"])
        print(lowest_med_owner_occupied)
        print(Boston.describe())
        print(Boston.describe()['rm'])
        # the only predictors that stand out when comparing the medv-smallest among ALL subburbs is crime being way higher than mean (3.6)
    ten_i = True
    if ten_i:
        # more rooms == higher medv ($$), newer homes, ?????
        lt_4_rooms = Boston.loc[lambda df: df["rm"] <= 4]
        gt_7_rooms = Boston.loc[lambda df: df["rm"] >= 7]
        gt_8_rooms = Boston.loc[lambda df: df["rm"] >= 8]
        print(lt_4_rooms.describe())
        print(gt_7_rooms.describe())
        print(gt_8_rooms.describe())
    exit()

