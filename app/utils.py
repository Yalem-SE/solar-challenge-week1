import matplotlib.pyplot as plt
import streamlit as st

# Plotting function
def plot_data(df, value_col, plot_style, moving_avg_on):
    fig, ax = plt.subplots(figsize=(12, 6))
    if plot_style == "Line Chart":
        ax.plot(df['Date'], df[value_col], label=value_col, color='tab:blue', alpha=0.8)
        if moving_avg_on and value_col in ['Value1', 'Value2']:
            mv_avg = df[value_col].rolling(window=7).mean()
            ax.plot(df['Date'], mv_avg, label='7-day Moving Avg', color='tab:orange')
        ax.set_ylabel(value_col)
        ax.set_xlabel("Date")
        ax.legend()
        ax.grid(True)
    elif plot_style == "Bar Chart":
        # Aggregate by Date
        grouped = df.groupby('Date')[value_col].mean().reset_index()
        ax.bar(grouped['Date'], grouped[value_col], color='tab:green', alpha=0.7)
        ax.set_ylabel(value_col)
        ax.set_xlabel("Date")
        ax.grid(axis='y')
    elif plot_style == "Scatter Plot":
        # Scatter between Value1 and Value2 for example
        color_col = 'Category'
        categories = df[color_col].astype('category').cat.codes
        scatter = ax.scatter(df['Value1'], df['Value2'], c=categories, cmap='viridis', alpha=0.7)
        ax.set_xlabel('Value1')
        ax.set_ylabel('Value2')
        legend_labels = df[color_col].unique()
        handles = [plt.Line2D([], [], marker='o', color=scatter.cmap(scatter.norm(i)), linestyle='', 
                              label=cat) for i, cat in enumerate(legend_labels)]
        ax.legend(handles=handles, title=color_col)
        ax.grid(True)
    else:
        st.error("Unsupported plot type.")
        return
    st.pyplot(fig)
