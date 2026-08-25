import pandas as pd


def disease_summary(df):
    return df.groupby("Disease")["Cases"].sum().reset_index()


def yearly_summary(df):
    return df.groupby("Year")["Cases"].sum().reset_index()


def gender_summary(df):
    return df.groupby("Gender")["Cases"].sum().reset_index()


def region_summary(df):
    return df.groupby("Region")["Cases"].sum().reset_index()


def age_group_summary(df):
    return df.groupby("Age_Group")["Cases"].sum().reset_index()


def total_cases(df):
    return df["Cases"].sum()


def total_deaths(df):
    return df["Deaths"].sum()