import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_categorical_value_counts(df, categorical_cols):
    """
    Plots the value counts for each categorical column in a DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the categorical columns.
    categorical_cols (list): List of column names to plot.
    """
    n = len(categorical_cols)

    cols = 3
    rows = math.ceil(n / cols) 


    fig, axes = plt.subplots(rows, cols, figsize=(6*cols, 6*rows))
    axes = axes.flatten()

    for i, col in enumerate(categorical_cols):
        df[col].value_counts().plot(kind="bar", ax=axes[i])
        axes[i].set_title(f"Value counts for {col}")
        axes[i].set_xlabel(col)
        axes[i].set_ylabel("Count")
        axes[i].margins(y=0.1)                      # add spacing

    fig.tight_layout(pad=3.0)


    # Hide unused subplots if any
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
    return fig

def plot_categorical_proportions(df, categorical_cols, target_col, palette="husl"):
    """
    Plots the proportions for each categorical column in a DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the categorical columns.
    categorical_cols (list): List of column names to plot.
    """
    palette = sns.color_palette(palette)

    for col in categorical_cols:
        contingency_table = pd.crosstab(df[col], df[target_col], normalize='index')
        
        sns.set_theme(style="whitegrid")
        
        # Pass palette colors to Pandas plot
        ax = contingency_table.plot(
            kind="bar",
            stacked=True,
            figsize=(20, 4),
            color=palette
        )
        
        ax.set_title(f"Percentage Distribution of {target_col} across {col}")
        ax.set_xlabel(col)
        ax.set_ylabel("Percentage")
        ax.legend(title=target_col)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

