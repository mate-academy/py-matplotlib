import pandas as pd
import matplotlib.pyplot as plt


def visualize_customer_data() -> None:
    df = pd.read_csv("data/customer_data.csv")
    
    # Simple plotting example based on customer data
    if "age" in df.columns and "income" in df.columns:
        plt.figure(figsize=(8, 6))
        plt.scatter(df["age"], df["income"], alpha=0.5)
        plt.title("Age vs Income")
        plt.xlabel("Age")
        plt.ylabel("Income")
        plt.savefig("app/plot.png")
        plt.close()


if __name__ == "__main__":
    visualize_customer_data()

