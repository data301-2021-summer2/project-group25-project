import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process('/users/annabelle/School/2021/Summer2/data301/group25-project/project-group25-project/data/raw/world-happiness-report-2021.csv'):
    df1=(pd.read_csv('/users/annabelle/School/2021/Summer2/data301/group25-project/project-group25-project/data/raw/world-happiness-report-2021.csv')
           .rename(columns = {'Ladder score':"Happiness score"})
           .assign(year='2021')
           .drop(['Logged GDP per capita', 
                              'Social support',
                              'Healthy life expectancy',
                              'Freedom to make life choices',
                              'Generosity',
                              'Perceptions of corruption',
                              'Ladder score in Dystopia',
                              'upperwhisker',
                              'lowerwhisker',
                              'Standard error of ladder score',
                              'Regional indicator',
                              'Dystopia + residual'],axis='columns')
           .rename(columns = {'Standard error of ladder score':"Standard error of happiness score", 
                          'Explained by: Log GDP per capita':"Log GDP per capita", 
                          'Explained by: Social support':"Social support", 
                          'Explained by: Healthy life expectancy':"Healthy life expectancy",
                          'Explained by: Freedom to make life choices':"Freedom to make life choices",
                          'Explained by: Generosity':"Generosity",
                          'Explained by: Perceptions of corruption':"Perceptions of corruption"}))
    return df1


def load_and_process('/users/annabelle/School/2021/Summer2/data301/group25-project/project-group25-project/data/raw/world-happiness-report.csv'):
    df2 = (pd.read_csv('/users/annabelle/School/2021/Summer2/data301/group25-project/project-group25-project/data/raw/world-happiness-report.csv')
           .rename(columns = {'Life Ladder':"Happiness score",'Healthy life expectancy at birth':"Healthy life expectancy"})
           .drop(['Positive affect','Negative affect'],axis='columns')
           .loc[lambda x: x['year']>2018])
    df3 = (df2
          .dropna(subset['Log GDP per capita'], inplace=True)
          .fillna(method ='pad')
          .reset_index(drop=True))  
    return df3