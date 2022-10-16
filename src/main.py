import smartD
import pandas as pd

def main():

    data = {'product_name': ['laptop', 'printer', 'tablet', 'desk', 'chair', 'wheel'],
            'price': [1200, 150, 300, 450, 200, 200]
            }

    df = pd.DataFrame(data)

    smartDataObj = smartD.SmartD(df,1)

if __name__ == "__main__":
    main()
